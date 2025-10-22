undefined_keys = [
    'KEY_FULL_SCREEN',
    'KEY_ASPECT_RATIO',
    'KEY_NOTIFICATION_CENTER',
    'KEY_PICKUP_PHONE',
    'KEY_HANGUP_PHONE',
    'KEY_FN_RIGHT_SHIFT',
    'BTN_GRIPL',
    'BTN_GRIPR',
    'BTN_GRIPL2',
    'BTN_GRIPR2',
    'KEY_KBD_LAYOUT_NEXT',
    'KEY_EMOJI_PICKER',
    'KEY_PRIVACY_SCREEN_TOGGLE',
    'KEY_SELECTIVE_SCREENSHOT',
    'KEY_MACRO1',
    'KEY_MACRO2',
    'KEY_MACRO3',
    'KEY_MACRO4',
    'KEY_MACRO5',
    'KEY_MACRO6',
    'KEY_MACRO7',
    'KEY_MACRO8',
    'KEY_MACRO9',
    'KEY_MACRO10',
    'KEY_MACRO11',
    'KEY_MACRO12',
    'KEY_MACRO13',
    'KEY_MACRO14',
    'KEY_MACRO15',
    'KEY_MACRO16',
    'KEY_MACRO17',
    'KEY_MACRO18',
    'KEY_MACRO19',
    'KEY_MACRO20',
    'KEY_MACRO21',
    'KEY_MACRO22',
    'KEY_MACRO23',
    'KEY_MACRO24',
    'KEY_MACRO25',
    'KEY_MACRO26',
    'KEY_MACRO27',
    'KEY_MACRO28',
    'KEY_MACRO29',
    'KEY_MACRO30',
    'KEY_MACRO_RECORD_START',
    'KEY_MACRO_RECORD_STOP',
    'KEY_MACRO_PRESET_CYCLE',
    'KEY_MACRO_PRESET1',
    'KEY_MACRO_PRESET2',
    'KEY_MACRO_PRESET3',
    'KEY_KBD_LCD_MENU1',
    'KEY_KBD_LCD_MENU2',
    'KEY_KBD_LCD_MENU3',
    'KEY_KBD_LCD_MENU4',
    'KEY_KBD_LCD_MENU5',
    'REL_WHEEL_HI_RES',
    'REL_HWHEEL_HI_RES',
    'ABS_PROFILE',
    'SW_MACHINE_COVER'
]

def modify_ecodes_c(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    for line in lines:
        added = False
        for key in undefined_keys:
            if f'PyModule_AddIntMacro(m, {key});' in line:
                modified_lines.append(f'#ifdef {key}\n')
                modified_lines.append(line)
                modified_lines.append('#endif\n')
                added = True
                break
        if not added:
            modified_lines.append(line)

    with open(file_path, 'w') as f:
        f.writelines(modified_lines)

if __name__ == "__main__":
    modify_ecodes_c('src/evdev/ecodes.c')
    print('Modified ecodes.c with #ifdef checks for undefined keys.')