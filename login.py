usuarios = {
    "franco": "1234",
    "admin": "adminpass",
    "invitado": "guest"
}

def validar():
    print("=== LOGIN ===")
    nick = input("Usuario: ")
    clave = input("Contraseña: ")
    
    if nick in usuarios and usuarios[nick] == clave:
        print(f"✔️ Bienvenido, {nick}")
        return True, nick
    else:
        print("❌ Usuario o contraseña incorrectos.")
        return False, None

if __name__ == "__main__":
    validar()