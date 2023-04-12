# eswap_remap_back_buttons

***Disclaimer: This is not officially supported by ThrustMaster - this is at your own risk. Brick your controller thats on you.***

TL;TL;DR ESwap X Pro can't map back buttons to useful things. Made it do it anyways.

TL;DR Purchased ESwap X Pro to play Rocket League since I was tired of replacing DS5s due to stick drift every 3-6 months. Thought it would be cool to map M4 to do a stall in Rocket League (DAR + Opposite DPAD + Jump), disappointed that back buttons could only be mapped to buttons I was already using. Briefly went down the USB protocol/driver dll injection rabbit hole, realized that ThrustMapperX allows export/import of preset profiles. With some testing figured out what mapped where and was able to map back buttons to other unused buttons on the controller (View button for example). After doing this was able to leverage third party tool to map the profile button press (now on M4 as well) using AntiMicroX to keyboard and mouse buttons (D + Q + Right Mouse Click). Now can use M4 to do stall in Rocket League. Win.

# Summary

A set of steps to remap the back buttons on the ESwap X Pro Controller. Note that this only allows remapping of the back buttons to other physical buttons on the controller itself, at first glance this seems not useful, however there other buttons on the controller that don't get any use in a PC environment or in the context of the average user (How many profiles do you actually use ?). 

The buttons in question are:

- View
- Menu

These buttons in a PC environment with the exception of Menu button don't often get used for anything.

Ultimately the approach is to map M4 to View, and then use AntiMicroX to map View to (D + Q + Right Click).

M4 -> View -> D + Q + Right Click

This is achievable using ThrustMapperX and JoyToKey.

My device is currently running:

Firmware: 63.0
Driver: 1.0.37
ThrustMapperX: 1.0.4.0


# Steps

1. Install 'ThrustMapperX' from the Microsoft store. I know it sucks but I couldn't find any other easy way to update profiles on the controller itself.

2. Plug-in your controller.

3. Open 'ThrustMapperX', make sure everything works as intended. Recognizes controller, update firmware, load/switch profiles, remap some buttons.

4. From the 'Home' screen in 'ThrustMapperX', click the three lines beside 'Profile 1' and select 'Duplicate' profile, give it a useful name and click 'Duplicate'.

![Duplicate Profile 1 for editting.](/images/duplicate_profile.png)

5. Click the three lines beside the new profile you have created, and select 'Export'. Save as a text file to somewhere.
![Export the newly created profile for editting.](/images/potato_profile_export.png)

6. Open that text file in the text editor of your choice (notepad is fine). This is a json formated file and will not show up great - but it doesn't really matter for our purposes.

![Open newly created profile in a text editor.](/images/notepad_profile_open.png)

7. You will want to search for the button mapping you are interested in remapping.

For example to remap 'M4', we will be modifying the following block of JSON:

```
"ButtonMappingStates19":{
"ControlId":19,
"LogicalOutMappingId":19,
"PhysicalInButtonControlId":15
}
```

Here is a list of the relevant mappings for the back buttons:

| Back Button | ButtonMappingStates |
|-|-|
| M1 | ButtonMappingStates16 |
| M2 | ButtonMappingStates17 |
| M3 | ButtonMappingStates18 |
| M4 | ButtonMappingStates19 |

8. Now that you have located the block of JSON you want to modify, we will change the 'PhysicalInButtonControlId' value to remap it to another button.

The following table outlines what other buttons maybe useful:

| Button | PhysicalInButtonControlId | AntiMicroX Mapping | JoyToKey Mapping |
|-|-|-|-|
| View | 5 | Back | Button 7 |
| Menu | 4 | Start | Button 8 |

As we are trying to map the 'View' button to 'M4' our JSON becomes:

```
"ButtonMappingStates19":{
"ControlId":19,
"LogicalOutMappingId":19,
"PhysicalInButtonControlId":5
}
```

Save this file.

9. Now in 'ThrustMapperX', click the three lines next to the new profile you created, and click "Load on profile 1". This should pop a window indicating that it was successfully loaded. You should also be able to see the name of the new profile after "Profile 1 (new profile name)".

10. You can now click the 'Mapping' next to the 'Home' icon, and you should see that 'M4' is now mapped to '?'.

![M4 map has changed.](/images/m4_map_changed.png)

11. You can further verify this by looking in whatever third party tool (AntiMicroX/JoyToKey/etc) you will use for the keyboard mapping portion to verify that it is actually properly mapped. You can also now map your button to whatever keyboard/mouse/other inputs you want.

![Mapped and activated in AntiMicroX](/images/key_mapped_antimicrox.png)

# Additional Notes

I did attempt get the guide button working as it appears to be supported on PC, however I could not find a ControlID/ButtonMappingStates value for that button, searched up to 300.

You can usually get out of a broken state by plugging the controller in while holding down the 'Map' key, found this out when I had a failed firmware update and the controller wouldn't stay powered on after plugging in.

There may be some additional value realized by leveraging JoyToKey's alias feature, ymmv.

## Third party mapping tools 

[AntiMicroX](https://github.com/AntiMicroX/antimicrox)

[JoyToKey](https://joytokey.net/)

## Other tools used

[HidReportInspector](https://github.com/Ryochan7/HidReportInspector)
