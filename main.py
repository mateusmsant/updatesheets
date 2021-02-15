import gspread

client = gspread.service_account(filename='credentials.json')
sheets = client.open_by_key('1QKWucXg-67pLjIF_uJuLFIOXh8upCh8Fo4R-ryZdkUg')
worksheet = sheets.sheet1

totalStudents = len(worksheet.get_all_values())
studentIndex = 4

def updateStatus():
  finalScore = 0
  absences = int(rows[2]) if rows[2].isnumeric() else print('Invalid input')

  if (absences/60 > 0.25):
    status = 'Reprovado por falta'
  else:
    notas = int(rows[-1]) + int(rows[-2]) + int(rows[-3])
    average = notas/3

    if average > 70:
      status = 'Aprovado'
    elif 50 <= average < 70:
      status = 'Exame final'
      finalScore = 100 - average
    else:
      status = 'Reprovado por nota'

  worksheet.update_cell(studentIndex, 7, status)
  worksheet.update_cell(studentIndex, 8, finalScore)  

while totalStudents >= studentIndex:
  rows = worksheet.row_values(studentIndex)
  
  updateStatus()

  studentIndex += 1