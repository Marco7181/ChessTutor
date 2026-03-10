import pygame
import chess

# 1. INIZIALIZZAZIONE (Dobbiamo farlo prima di tutto)
pygame.init()

# 2. DEFINIZIONE COSTANTI (Nomi che useremo dopo)
LARGHEZZA, ALTEZZA = 600, 600
DIM_CASA = LARGHEZZA // 8
BIANCO = (235, 235, 208)
VERDE = (119, 149, 86)

# 3. CREAZIONE FINESTRA
SCHERMO = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Il mio Tutor di Scacchi")

def disegna_scacchiera(superficie):
    """Questa funzione disegna i quadrati"""
    for riga in range(8):
        for colonna in range(8):
            # Se la somma di riga e colonna è pari, il colore è bianco
            colore = BIANCO if (riga + colonna) % 2 == 0 else VERDE
            pygame.draw.rect(superficie, colore, (colonna * DIM_CASA, riga * DIM_CASA, DIM_CASA, DIM_CASA))

def main():
    """Funzione principale che tiene aperta la finestra"""
    board = chess.Board()
    running = True

    while running:
        # Controlla se l'utente clicca sulla X per chiudere
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
        
        # Disegna la scacchiera
        disegna_scacchiera(SCHERMO)
        
        # Aggiorna il monitor
        pygame.display.flip()

    pygame.quit()

# 4. AVVIO DEL PROGRAMMA
if __name__ == "__main__":
    main()
