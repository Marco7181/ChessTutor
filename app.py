import pygame
import chess
import os

pygame.init()
LARGHEZZA, ALTEZZA = 600, 600
DIM_CASA = LARGHEZZA // 8
SCHERMO = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Tutor Scacchi")

IMMAGINI = {}

def carica_immagini():
    pezzi = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for pezzo in pezzi:
        percorso = os.path.join("images", f"{pezzo}.png")
        try:
            img = pygame.image.load(percorso)
            IMMAGINI[pezzo] = pygame.transform.scale(img, (DIM_CASA, DIM_CASA))
        except Exception as e:
            print(f"Errore: Non trovo l'immagine {percorso}. Assicurati che esista!")

def disegna_scacchiera(superficie):
    for r in range(8):
        for c in range(8):
            colore = (235, 235, 208) if (r + c) % 2 == 0 else (119, 149, 86)
            pygame.draw.rect(superficie, colore, (c * DIM_CASA, r * DIM_CASA, DIM_CASA, DIM_CASA))

def disegna_pezzi(superficie, board):
    for r in range(8):
        for c in range(8):
            casa = chess.square(c, 7 - r)
            pezzo = board.piece_at(casa)
            if pezzo:
                colore = 'w' if pezzo.color == chess.WHITE else 'b'
                nome = colore + pezzo.symbol().upper()
                if nome in IMMAGINI:
                    superficie.blit(IMMAGINI[nome], (c * DIM_CASA, r * DIM_CASA))

def main():
    carica_immagini()
    board = chess.Board()
    running = True
    
    casa_selezionata = None  # Memorizza dove hai cliccato la prima volta

    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
            
            # Gestione del Clic del Mouse
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posizione = pygame.mouse.get_pos() # Coordinate (x, y) in pixel
                colonna = posizione[0] // DIM_CASA
                riga = posizione[1] // DIM_CASA
                
                # Convertiamo le coordinate del mouse in una casa di scacchi (0-63)
                casa_cliccata = chess.square(colonna, 7 - riga)

                if casa_selezionata is None:
                    # Se è il primo clic, selezioniamo il pezzo (se c'è)
                    if board.piece_at(casa_cliccata):
                        casa_selezionata = casa_cliccata
                else:
                    # Se avevamo già selezionato un pezzo, proviamo a muoverlo
                    mossa = chess.Move(casa_selezionata, casa_cliccata)
                    
                    # Controlliamo se la mossa è legale (secondo le regole degli scacchi)
                    if mossa in board.legal_moves:
                        board.push(mossa) # Esegue la mossa sulla scacchiera
                    
                    casa_selezionata = None # Reset della selezione dopo il tentativo

        disegna_scacchiera(SCHERMO)
        disegna_pezzi(SCHERMO, board)
        
        # Opzionale: Evidenzia la casa selezionata
        if casa_selezionata is not None:
            c, r = chess.square_file(casa_selezionata), 7 - chess.square_rank(casa_selezionata)
            pygame.draw.rect(SCHERMO, (255, 255, 0), (c * DIM_CASA, r * DIM_CASA, DIM_CASA, DIM_CASA), 4)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
