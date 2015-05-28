import sys
from game import State

from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, \
    QWidgetItem, QSpacerItem


class Communicate(QObject):
    
    flag = pyqtSignal()
    open = pyqtSignal()
    neighbours = pyqtSignal()


class Tile(QLabel):

    tile_size = 30

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(self.tile_size, self.tile_size)
        self.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        self.com.position = self.position
        button = event.button()

        if button == Qt.RightButton:
            self.com.flag.emit()
        elif button == Qt.MiddleButton:
            self.com.neighbours.emit()
        else:
            self.com.open.emit()

    def setStyleOpened(self):
        pass

    def setStyleClosed(self):
        self.setStyleSheet("""QLabel {
            background-color : blue;
            color : white;
        }""")


class Board(QWidget):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.width, self.height = self.game.dimensions()

        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(1)
        self.com = Communicate()
        self.com.flag.connect(self.tileFlagged)
        self.com.open.connect(self.tileOpened)
        self.com.neighbours.connect(self.tileOpenNeighbours)

        self.draw()

    def draw(self):
        grid = self.layout()
        width, height = self.width, self.height

        for y in range(height):
            for x in range(width):

                if self.game.is_opened((x, y)):
                    value = self.game.value_at_position((x, y))
                    if not value:
                        continue

                    valueLabel = Tile(str(value))
                    valueLabel.setStyleOpened()
                    valueLabel.position = (x, y)
                    valueLabel.com = self.com
                    grid.addWidget(valueLabel, x, y)
                    continue

                text = ''
                if self.game.is_flagged((x, y)):
                    text = '⚑'

                tile = Tile(text)
                tile.position = (x, y)
                tile.com = self.com
                tile.setStyleClosed()
                grid.addWidget(tile, x, y)

        label = QLabel('Game state: {}'.format(self.game.state.value))
        grid.addWidget(label, height, 0, 1, width)

    def tileOpened(self):
        if self.game.state is not State.running:
            return

        sender = self.sender()
        position = sender.position
        self.game.open_position(position)
        self.clear_layout(self.layout())
        self.draw()

    def tileFlagged(self):
        if self.game.state is not State.running:
            return

        sender = self.sender()
        position = sender.position
        self.game.flag_position(position)
        self.clear_layout(self.layout())
        self.draw()

    def tileOpenNeighbours(self):
        if self.game.state is not State.running:
            return

        sender = self.sender()
        position = sender.position
        self.game.open_neighbours(position)
        self.clear_layout(self.layout())
        self.draw()

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)

            if isinstance(item, QWidgetItem):
                item.widget().close()
                # or
                # item.widget().setParent(None)
            elif isinstance(item, QSpacerItem):
                pass
                # no need to do extra stuff
            else:
                self.clear_layout(item.layout())

            # remove the item from layout
            layout.removeItem(item)


class UserInterface:
    def __init__(self, game):
        self.game = game

    def main_loop(self):
        app = QApplication(sys.argv)

        w = Board(self.game)
        w.move(300, 300)
        w.setWindowTitle('Pysweeper')
        w.show()
        
        app.exec_()
