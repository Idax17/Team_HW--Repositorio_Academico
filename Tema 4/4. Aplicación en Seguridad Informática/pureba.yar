rule Deteccion_Malware {
    strings:
        $cadena1 = "cmd.exe /c"
        $hex_firma = { E2 34 A1 C8 23 FB }
    condition:
        $cadena1 or $hex_firma
}