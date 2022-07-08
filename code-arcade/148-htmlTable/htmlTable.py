def solution(table, row, column):
    try:
        table = table.split('<tr>')[row+1]
        table = table.split('<td>')[column+1]
        return table[:table.find('</')]
    except:
        return 'No such cell'