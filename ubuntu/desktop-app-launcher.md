Suppose that we have an executable that can be used from the terminal, such as
```
$ ./my-app.x
```
To create a desktop launcher that can run the app simply create a text file with the following content

```
[Desktop Entry]
Name=YourApp
Exec=/path/to/my-app.x
Icon=/path/to/icon.png
Comment=app
Type=Application
Terminal=false
Encoding=UTF-8
Categories=Utility;
```
The keys `Exec` and `Icon` must be replaced with the correct path to the excecutable and the image file.

Then, name the file `myapp.desktop` and save it into the Desktop folder.

Finally, right click on the newly created desktop launcher and click `Allow launching`.

Moreover, if we also want to add the launcher to our applications menu, simply copy the launcher to the `/usr/share/applications directory`.
```
sudo cp /path/to/myapp.desktop /usr/share/applications/
```

That's it!
