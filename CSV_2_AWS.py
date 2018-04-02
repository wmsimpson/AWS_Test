import boto

MY_ACCESS_KEY_ID = 'AKIAJRPYJGPDXBEEKDHA'
MY_SECRET_ACCESS_KEY = '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'

def do_batch_write(items, table_name, dynamodb_table, dynamodb_conn):
    batch_list = dynamodb_conn.new_batch_write_list()
    batch_list.add_batch(dynamodb_table, puts=items)
    while True:
        response = dynamodb_conn.batch_write_item(batch_list)
        unprocessed = response.get('UnprocessedItems', None)
        if not unprocessed:
            break
        batch_list = dynamodb_conn.new_batch_write_list()
        unprocessed_list = unprocessed[table_name]
        items = []
        for u in unprocessed_list:
            item_attr = u['PutRequest']['Item']
            item = dynamodb_table.new_item(
                attrs=item_attr
            )
            items.append(item)
        batch_list.add_batch(dynamodb_table, puts=items)


def import_csv_to_dynamodb(table_name, csv_file_name, col_names, column_types):
    '''
    Import a CSV file to a DynamoDB table
    '''
    dynamodb_conn = boto.connect_dynamodb(aws_access_key_id=MY_ACCESS_KEY_ID,
                                          aws_secret_access_key=MY_SECRET_ACCESS_KEY)
    dynamodb_table = dynamodb_conn.get_table(table_name)
    BATCH_COUNT = 7  # 25 is the maximum batch size for Amazon DynamoDB

    items = []

    count = 0
    csv_file = open(csv_file_name, 'r', encoding="utf-8-sig")
    for cur_line in csv_file:
        count += 1
        cur_line = cur_line.strip().split(',')

        row = {}
        for col_number, col_name in enumerate(col_names):
            row[col_name] = column_types[col_number](cur_line[col_number])

        item = dynamodb_table.new_item(
            attrs=row
        )
        items.append(item)

        if count % BATCH_COUNT == 0:
            print
            'batch write start ... ',
            do_batch_write(items, table_name, dynamodb_table, dynamodb_conn)
            items = []
            print
            'batch done! (row number: ' + str(count) + ')'

    # flush remaining items, if any
    if len(items) > 0:
        do_batch_write(items, table_name, dynamodb_table, dynamodb_conn)

    csv_file.close()


def main():
    col_names = 'Col1 Col2 Col3 Col4'.split()  # ["Data Element #", "Data Element Name", "MI_DB_Column_Name", "Description and Codes", "Format", "Required?", "Reference", "Transform", "Client Source", "Client Ref Source", "Used For", "Example(s)"]
    table_name = 'TestDB'
    csv_file_name = 'Test_Data.csv'
    column_types = [str, str, str, str]
    import_csv_to_dynamodb(table_name, csv_file_name, col_names, column_types)


if __name__ == "__main__":
    main()
    # cProfile.run('main()') # if you want to do some profiling