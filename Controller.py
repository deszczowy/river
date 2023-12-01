from Core import RConfig, RTimer
from Engine import RProject, RBuild
from Enums import EnProjectFile
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

class RController:
    def __init__(self, engine, view, config):
        self.project = None
        self.clock = None

        self.config = config
        self.engine = engine
        self.view = view

        self.load_project_object()
        self.setup_clock()

        self.bind_actions()
        self.bind_shortcuts()

    def load_project_object(self):
        """
        Method creates project management object.
        First projects root directory is loaded from config, then default project is loaded and 
        controller loads content into editors.
        """
        projects_root_directory = self.config.get_setting('project_root', './') # constants for config entries
        
        self.project = RProject(projects_root_directory)
        self.load_project("default")

    def setup_clock(self):
        """
        Method creates timer and connects some methods into it (for saving project and clearing message board).
        Then starts the timer.
        """
        self.clock = RTimer(self.view)
        self.clock.scheduled_method = self.save
        self.clock.timeout_method = self.clear_message
        self.clock.prepare()

    def save(self):
        """
        This method has global usage.
        It stores current project's data on disk using project manager.
        All action is triggered only if editors are modified.
        """
        if self.view.is_modified():
            # Collecting data from editors
            mainText = self.view.get_main_content()
            
            # Storing data in project files
            self.project.set(EnProjectFile.Flow, mainText) # todo: EnProjectFile.Flow is a internal project identifier, should not be used here on a controller level
            
            # Finalisation
            self.view.set_unmodified()
            self.view.show_message("Saved")
            self.clock.setup()

    def load_project(self, name):
        """
        This is internal controller method for atomic action of loading project provided by name.
        """
        # First, the manager object should switch it's focus on new project
        self.project.load_project(name) 
        # Second, project data is loaded into editors
        self.load_project_data_to_view()
        # and here we are - project loaded
        self.view.set_focus()
    
    def load_project_data_to_view(self):
        """
        This method uses project management object to get files contents
        and then loads them into editors. Also statusbar project info panel is updated.
        """
        # Reading project data
        name = self.project.get_current_name()
        main = self.project.get(EnProjectFile.Flow)
        #side = self.project.get(EnProjectFile.Note)
        
        # Loading content
        self.view.set_main_content(main)
        # Statusbar update
        self.view.set_project_info(name)
    
    def clear_message(self):
        """
        Sometimes a message is sent into statusbar message board. It is not intended to stay there forever, so
        this method is provided into timer timeout function to clear message board when it's time expires.
        """
        self.view.show_message("")
    
    def run_new_open(self):
        """
        This method has 'run_' prefix in name, so it is an action method, intended to be used in UI interactions.
        This particular method opens modal dialog which provides choice for an user, who can open existing project, 
        or create a new one.
        Then the project is loaded.
        """
        # Projects root directory is needed for dialog to properly load available projects
        path = self.project.get_root()
        
        # Dialog is part of a UI, so view is responsible for showing it
        data = self.view.open_new_action(path)

        if data != None:
            # if data is returned from dialog (!None) then controller will make an attempt to load selected project data
            # but first current project should be saved 
            self.save()

            # loading selected project
            name = data.name
            self.load_project(name)

            if data.new:
                self.project.update_header_file(data.title, data.author, data.description)
                print("New project created")
    
    def run_print(self):
        """
        Action method for printing.
        It calls printing dialog, and the rest action is done there.
        """
        # Project's build files location
        path = self.project.get_build_directory()

        # Calling print dialog with build path
        data = self.view.print_action(path)
        if data != None:
            print("Printing {0}".format(data))

            build = RBuild(path)
            build.print_main_text(self.view.get_main_content())

    def run_fullscreen_toggle(self):
        self.view.toggle_fullscreen()

    def run_sidenote_toggle(self):
        self.view.toggle_sidenote()

    def run_on_close(self):
        self.save()

    def bind_actions(self):
        """
        The only one method to bind all view events with coresponding actions.
        """
        self.view.on_close_method = self.run_on_close

    def bind_shortcuts(self):
        """
        The only one method to bind all shortcuts with coresponding actions
        """
        self.shortcutSave = QShortcut(QKeySequence("Ctrl+S"), self.view)
        self.shortcutOpenNew = QShortcut(QKeySequence("F2"), self.view)
        self.shortCutPrint = QShortcut(QKeySequence("F4"), self.view)
        self.shortCutSideNote = QShortcut(QKeySequence("F6"), self.view)
        self.shortCutFullscreen = QShortcut(QKeySequence("F7"), self.view)

        self.shortcutSave.activated.connect(self.save)
        self.shortcutOpenNew.activated.connect(self.run_new_open)
        self.shortCutPrint.activated.connect(self.run_print)
        self.shortCutSideNote.activated.connect(self.run_sidenote_toggle)
        self.shortCutFullscreen.activated.connect(self.run_fullscreen_toggle)

    