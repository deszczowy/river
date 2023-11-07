## Unsorted (but grouped) thoghts and ideas

Remember: all todos are tasks to plan, so should eventually land here

Remember: don't think too much, move on, there is plenty to do

Remember: incorporate prototype as quick as possible, then delete one

### Priorities for version 0.1
1. Creating new project
2. Printing main text
3. Build

### Prints
- printing of main text - page divided in two columns (and optionally right side is empty for hand notes) -> html
- prints have code name (project name) on a header
- font 9pt, minimal margins

### Functions
- projects backup
- [F1] help, directed to help page on gh.com
- project history/versions?
- defining custom theme
- aditional file for project with session state (cursor position, widgets toggled etc.)
- export/import through zip files
- saving on close!
- alarm to set if you want to be inform when to stop writing session

### UI
- (left) main menu. [Esc] key, button maybe. Simple with buttons, actions on keys. Buttons with pointer cursor and hover - simple and weby vibe. Option name + key
- side editor for random notes (right)
- statusbar center panel - description for menu, sidenote and preview
- statusbar left panel - project name + "#"'s count
- statusbar right panel - message board
- new project dialog
- open project dialog, with list of projects loaded from configured path
- options dialog
- UI by principle will not have clock BUT maybe alarm for ending session?
- fullscreen oprion, with small closing x for return besides keyboard shortcut)
- contrast theme, for working outside (should be tested in sunny garden ;)
- light theme - tested in day
- some light borders to widgets?
- little padding on statusbar panels
- project properties dialog

### Build
- texts in '[' and ']' will be presented as todo's
- special directory 'build' for build resutls in project location

### Keys
[Esc] - Main menu
[F1] - Help
[F2] - Open dialog
[F3] - Saving as new project dialog
[F4] - Print
[F5] - Build
[F6] - Toggle side
[F7] - Toggle fullscreen
[F8] - Options dialog
[F9] - Theme dark
[F10] - Theme light
[F11] - Theme contrast
[F12] - Theme custom
[Ctrl + S] - Save on demand

### Processes and notes
- F10 - F12 slots can be free if themes will be triggered in chain on F9 key, starting from dark, to custom and so on
- view classes chold have middleclasses to set/get data. Connectors
- how to get into config dirctory linux/windows
- deb packaging

### History database
- history.dat ? simple db, no chaos
- table for main text
- table for sidenotes
- simplicity, same structure

[id, content, saving_date, who_saved]

- header table, one row
[structure_version]

- connection class with structure update (check cursor thing, maybe could be used for update scripts)
- every saving store current text into db, if modified
- disk file has priority so opening process will be like
1. reading from file - content + modification time of file
2. reading last entry in db
3. if file content is different, then is loaded, then saved into history with who_saved = outside
4. [optionally] dates could be compared and newer version will be opened

- UI should have history preview with dates in left panel, text in main panel, and searching in text aplet
- and dialog with history options, like is every save stored, or how long should versions be stored