stylesheet = """

    /* Base components setup */

    QWidget
    {
        margin:0px; 
        padding:0px; 
        border:0px;
        background-color: #1E1E1E;
        color: #D4D4D4;
        font-size: 16px;
        font-family: 'Roboto Mono';
    }
    
    QLabel
    {
        font-size: 12px;
        color: #4E4E4E;
        color: white;
    }

    QLineEdit
    {
        border: 0px;
        border-bottom: 1px solid #8C8C8C;
        color: #D4D4D4;
    }

    QTextEdit
    {
        border: 0px;
        margin: 0px;
        padding: 0px;
        color: #fff;
        font-family: 'Roboto Mono';
    }

    QPushButton
    {
        font-size:12px;
        border: 0px; 
        min-width: 10px; 
        min-height: 10px; 
        padding: 3px;
        color: #D4D4D4;
    }

    /* Scrollbar */

    QScrollBar:vertical
    {
        border: 0;
        background-color: #1E1E1E;
        width:7px;
        margin: 0;
    }

    QScrollBar::handle:vertical
    {
        min-height: 0px;
        background-color: #8C8C8C;
        border-radius: 3px;
    }

    QScrollBar::add-line:vertical
    {
        height: 0px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }

    QScrollBar::sub-line:vertical
    {
        height: 0 px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
    {
        background: none;
    }

    /* Tabs */

    QTabWidget::pane
    {
        border: 0px solid red;
        padding: 0px;
        margin: 0px;
        background-color: #1E1E1E;
        color: #D4D4D4;
    }

    QTabWidget::tab-bar 
    {
        border: 0px;
        background-color: #1E1E1E;
        color: #D4D4D4;
        width: 300px;
    }

    QTabBar::tab {
    
        border: 0px;
        min-width: 70px;
        padding: 4px;
        background: black;
    }

    QTabBar::tab:selected {
        background-color: #1E1E1E;
        color: #D4D4D4;
    }

    QTabBar::tab:!selected {
        background: #1A1A1A;
        color: #4D4D4D;
    }

    QTabBar::tab:hover {
        font-weight: bold;
    }

    #StatusBar
    {
        font-size: 10px;
        color: #8C8C8C;
        padding: 5px;
        font-family: mono;
    }

    #StatusPanel
    {
        font-size: 10px;
        color: #bbb;
        padding: 10px;
    }
"""