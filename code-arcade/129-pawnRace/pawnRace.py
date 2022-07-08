def solution(white, black, toMove):
    winner = {'w': 'white',
              'b': 'black'}

    toPiece = lambda piece: [ord(piece[0])-ord('a'), int(piece[1])]
    whiteFile, whiteRank = toPiece(white)
    blackFile, blackRank = toPiece(black)

    # if on the same file and black is on a higher rank,
    # they'll bump and will not be able to pass eachother
    if(whiteFile == blackFile and blackRank > whiteRank):
        return 'draw'

    def canCapture(blackRank, blackFile, whiteRank, whiteFile):
        """return True if a piece can be captured"""
        return abs(blackFile - whiteFile) == 1 and \
               abs(whiteRank - blackRank) == 1 and \
               whiteRank < blackRank

    while True:
        # if piece can capture: return winner
        if canCapture(blackRank, blackFile, whiteRank, whiteFile):
            return winner[toMove]

        # else move
        if toMove == 'w':
            if whiteRank != 2 or \
               canCapture(blackRank, blackFile, whiteRank + 2, whiteFile):
                whiteRank += 1
            else:
                whiteRank += 2

        if toMove == 'b':
            if blackRank != 7 or \
               canCapture(blackRank - 2, blackFile, whiteRank, whiteFile):
                blackRank -= 1
            else:
                blackRank -= 2

        # if piece is on promotion square: return winner
        if whiteRank == 8 or blackRank == 1:
            return winner[toMove]

        toMove = 'w' if toMove == 'b' else 'b'
