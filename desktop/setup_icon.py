

class DesktopIcon:

    file = None
    name = None
    exec = None
    icon = None

    def to_desktop_icon(self):
        with open(self.file, "w") as file:
            file.write(f"#!/usr/bin/env xdg-open"\n
                "[Desktop Entry]"\n
                "Type=Application"\n
                "Terminal=false"\n
                "Encoding=UTF-8"\n
                "Version=1.1"\n
                "Categories=Development;IDE;Programming"\n
                "StartupNotify=true"\n\n
                "Name={self.name}"\n
                "Name[en_GB]={self.name}"\n
                "Exec=env GTK_IM_MODULE=ibus {self.exec}"\n
                "Icon={self.icon}"\n)
    