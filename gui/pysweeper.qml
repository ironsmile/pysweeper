//import related modules
import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Window 2.2

//window containing the application
ApplicationWindow {

    //title of the application
    title: qsTr("Pysweeper")
    width: 640
    height: 640

    //menu containing two menu items
    menuBar: MenuBar {
        Menu {
            title: qsTr("&Game")
            MenuItem {
                text: qsTr("&New")
                onTriggered: console.log("New game requested");
            }
            MenuItem {
                text: qsTr("E&xit")
                onTriggered: Qt.quit();
            }
        }
    }

    //Content Area 
}
