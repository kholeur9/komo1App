import openpyxl
from client.models import Client, Forfait

def send_data(file_path):
    workbook = openpyxl.load_workbook(file_path)

    sheet = workbook.active

    column_names = [cell.value for cell in sheet[1]]

    msisdn_col = column_names.index('MSISDN') + 1
    volume_col = column_names.index('VOLUME_') + 1
    date_t_col = column_names.index('DATE_T') + 1

    for row in sheet.iter_rows(min_row=2, values_only=True):
        msisdn, volume, date_t= row[msisdn_col - 1], row[volume_col - 1], row[date_t_col - 1]
        
        client, created = Client.objects.get_or_create(numero=msisdn)

        forfait_client_instance = Forfait(
            client=client,
            forfait=volume,
            date=date_t
        )
        forfait_client_instance.save()

    workbook.close()