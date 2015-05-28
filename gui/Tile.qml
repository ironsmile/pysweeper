// Represents a Tile

import QtQuick 2.3

Rectangle {
    width: 50; height: 50
    color: "blue"
    radius: 8

    MouseArea {
        anchors.fill: parent
        onClicked: console.log("Tile clicked!")
    }
}

