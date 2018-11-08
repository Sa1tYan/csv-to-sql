import csv
from tqdm import tqdm

'''
This script takes a CSV file with a mandatory header and a sql tablename and converts the data in the csv file into
an SQL INSERT statement.
'''

class CsvToSql(object):

    def __init__(self):
        # sql data will generate in your file_path.
        file_path = input('please insert your convert data path: ')
        db = input('please your database name: ')
        sql_file = file_path.split('.csv')[0] + '.sql'
        self.file = open(sql_file, 'w', encoding='utf-8')
        self.db = db
        self.file_path = file_path

    def get_data(self):
        with open(self.file_path, encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_ALL )
            header = next(reader)
            insert_str = 'INSERT INTO ' + '`' + self.db + '`' +'('
            for i in header:
                insert_str += '`' + i + '`,'
            insert_str = insert_str[:-1] + ')\n'
            insert_str += '\tVALUES\n\t\t('
            for items in tqdm(reader):
                item_str = ''
                for item in items:
                    item_str += "'"  + item.replace("'", "''") + "',"
                t_str = insert_str + item_str[:-1] + ');\n'
                self.file.write(t_str)

    def run(self):
        self.get_data()


if __name__ == '__main__':
    cs = CsvToSql()
    cs.get_data()