## Resize Icon For STM32CubeIDE

### Operating environment

- Python 3.8.x
  - pip
  - wxPython
  - pillow 



### Description

Because the toolbar icons of STM32CubeIDE are too small, it is almost impossible to see what they are on a 4K monitor, so there is this tool to adjust their size.

Please use the **`Browse`** button to specify the installation directory of STM32CubeIDE, and then use the **`Perform Adjustments`** button in the lower left corner to modify the size of those icons.

You can use the **`Revert`** button to restore those icons. (Size: 16*16)

**Note** that every modified icon will have a backup with the prefix ***" old_ "*** added.



### Instructions

```shell
python BigIcon.py
```

So you only need to download **`BigIcon.py`**, unless you plan to beautify its UI, then other files are needed.



<img src="Image/image-20210406090624647.png" alt="image-20210406090624647" style="zoom: 80%;" />