<<<<<<< HEAD
import psycopg2
import data


def main():
    conn = psycopg2.connect("postgresql://tvdi_piwl_user:6khvgKZfZEjoce0jmn4711t8tGmoXeed@dpg-cpscsul6l47c73e3h7a0-a.singapore-postgres.render.com/tvdi_piwl")

    #with conn自動commit
    with conn:
        with conn.cursor() as cursor: #自動close()
            sql = '''
            create table if not exists youbike(
                _id serial primary key,
                sna varchar(50) not null,
                sarea varchar(50),
                ar varchar(100),
                mday timestamp,
                updateTime timestamp,
                total smallint,
                rent_bikes smallint,
                return_bikes smallint,
                lat real,
                lng real,
                act boolean
            );
            '''
            cursor.execute(sql)
    all_data:list[dict] = data.load_data()

    with conn:
        with conn.cursor() as cursor: #自動close()
            insert_sql = '''
                insert into youbike(act,ar,lat,lng,mday,rent_bikes,return_bikes,sarea,sna,total,updateTime)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                '''
            
            for site in all_data:
                cursor.execute(insert_sql,( site['act'],site['ar'], site['lat'],site['lng'], site['mday'], site['rent_bikes'],site['retuen_bikes'],  site['sarea'], site['sna'], site['total'],site['updateTime'],))
    conn.close()

if __name__ == '__main__':
=======
import psycopg2
import data


def main():
    conn = psycopg2.connect("postgresql://tvdi_piwl_user:6khvgKZfZEjoce0jmn4711t8tGmoXeed@dpg-cpscsul6l47c73e3h7a0-a.singapore-postgres.render.com/tvdi_piwl")

    #with conn自動commit
    with conn:
        with conn.cursor() as cursor: #自動close()
            sql = '''
            create table if not exists youbike(
                _id serial primary key,
                sna varchar(50) not null,
                sarea varchar(50),
                ar varchar(100),
                mday timestamp,
                updateTime timestamp,
                total smallint,
                rent_bikes smallint,
                return_bikes smallint,
                lat real,
                lng real,
                act boolean
            );
            '''
            cursor.execute(sql)
    all_data:list[dict] = data.load_data()

    with conn:
        with conn.cursor() as cursor: #自動close()
            insert_sql = '''
                insert into youbike(act,ar,lat,lng,mday,rent_bikes,return_bikes,sarea,sna,total,updateTime)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                '''
            
            for site in all_data:
                cursor.execute(insert_sql,( site['act'],site['ar'], site['lat'],site['lng'], site['mday'], site['rent_bikes'],site['retuen_bikes'],  site['sarea'], site['sna'], site['total'],site['updateTime'],))
    conn.close()

if __name__ == '__main__':
>>>>>>> f360f313d7ecd36d29cee00b328690e0d221a97a
    main()