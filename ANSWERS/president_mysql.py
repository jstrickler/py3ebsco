import pymysql


class President(object):
    PRES_QUERY = '''
    select num, lname, fname, dstart, dend, birthplace, birthstate,
        dbirth, ddeath, party
    from presidents
    where num = %s
    '''

    def __init__(self, index):
        self._get_data(index)

    def _get_data(self, index):
        conn = pymysql.connect(
            host="localhost",
            db="python2",
            user="scripts",
            passwd="scripts"
        )
        cur = conn.cursor()
        row_count = cur.execute(President.PRES_QUERY, (index,))
        if row_count == 1:
            row = cur.fetchone()
            self._termnum = row[0]
            self._lname = row[1]
            self._fname = row[2]
            self._ts_date = row[3]
            self._te_date = row[4]
            self._bplace = row[5]
            self._bstate = row[6]
            self._bdate = row[7]
            self._ddate = row[8]
            self._party = row[9]
        else:
            print("Term {} not found".format(index))

    @property
    def last_name(self):
        return self._lname

    @property
    def first_name(self):
        return self._fname

    @property
    def birth_date(self):
        return self._bdate

    @property
    def death_date(self):
        return self._ddate

    @property
    def birth_place(self):
        return self._bplace

    @property
    def birth_state(self):
        return self._bstate

    @property
    def term_start(self):
        return self._ts_date

    @property
    def term_end(self):
        return self._te_date

    @property
    def party(self):
        return self._party


if __name__ == '__main__':
    for term in 1, 16, 26, 44, 45:
        p = President(term)
        print(p.first_name, p.last_name, p.party)
