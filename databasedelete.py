def delete():
    # creat database
    conn = sqlite3.connect('address_book.db')

    #creat cursor
    c.execute("DELETE from address WHERE oid = " + delete_box.get())
    print('Deleted sucessfully')

    #query of the database
    c.ececute("SELECT *, oid FROM addresses")

    record = c.fetechall
    # print(records)

    #loop through the results
    print_record = ''
    for record in records:
        #str(record[6]) added for displaying the id
        print_record += str(record[0]) + '' + str(record[1]) + '' + '\t' + str(record[6])

    query_label = Label(root, text=print_record)
    query_label.grid(row=11, colomn=0, columnspan=2)

    conn.commit()
    conn.close()
