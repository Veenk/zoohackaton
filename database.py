import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="name",
  password="1234",
  database = "suspects"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE suspects (Suspect_id int NOT NULL AUTO_INCREMENT, name VARCHAR(255),surname VARCHAR(255), address VARCHAR(255), content VARCHAR(255), images VARCHAR(255), facebook VARCHAR(255))")
# mycursor.execute("ALTER TABLE suspects ADD suspect_id INT PRIMARY KEY AUTO_INCREMENT")
sql = "INSERT INTO suspects (name, surname, address, content, images, facebook) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
  ('Peter', 'Smith' , 'Lowstreet 4', 'some long string1', '', ''),
  ('Amy', 'Adams' , 'Apple st 652','some long string2','', ''),
  ('Hannah', 'Montana',' Mountain 21', 'some long string3','', ''),
  ('Michael', 'Corse', 'Valley 345', 'some long string4','', '' ),
  ('Sandy', 'Mandy', 'Ocean blvd 2', 'some long string5','', ''),
  ('Betty', 'Bet', 'Green Grass 1', 'some long string6','', ''),
  ('Richard', 'Rich', 'Sky st 331', 'some long string7','', ''),
  ('Peter', 'Smith' , 'Lowstreet 4', 'some long string1', '', ''),
  ('Amy', 'Adams' , 'Apple st 652','some long string2','', ''),
  ('Hannah', 'Montana',' Mountain 21', 'some long string3','', ''),
  ('Michael', 'Corse', 'Valley 345', 'some long string4','', '' ),
  ('Sandy', 'Mandy', 'Ocean blvd 2', 'some long string5','', ''),
  ('Betty', 'Bet', 'Green Grass 1', 'some long string6','', ''),
  ('Richard', 'Rich', 'Sky st 331', 'some long string7','', ''),
('Peter', 'Smith' , 'Lowstreet 4', 'some long string1', '', ''),
  ('Amy', 'Adams' , 'Apple st 652','some long string2','', ''),
  ('Hannah', 'Montana',' Mountain 21', 'some long string3','', ''),
  ('Michael', 'Corse', 'Valley 345', 'some long string4','', '' ),
  ('Sandy', 'Mandy', 'Ocean blvd 2', 'some long string5','', ''),
  ('Betty', 'Bet', 'Green Grass 1', 'some long string6','', ''),
  ('Richard', 'Rich', 'Sky st 331', 'some long string7','', ''),
  ('Peter', 'Smith' , 'Lowstreet 4', 'some long string1', '', ''),
  ('Amy', 'Adams' , 'Apple st 652','some long string2','', ''),
  ('Hannah', 'Montana',' Mountain 21', 'some long string3','', ''),
  ('Michael', 'Corse', 'Valley 345', 'some long string4','', '' ),
  ('Sandy', 'Mandy', 'Ocean blvd 2', 'some long string5','', ''),
  ('Betty', 'Bet', 'Green Grass 1', 'some long string6','', ''),
  ('Richard', 'Rich', 'Sky st 331', 'some long string7','', ''),
  ('Peter', 'Smith' , 'Lowstreet 4', 'some long string1', '', ''),
  ('Amy', 'Adams' , 'Apple st 652','some long string2','', ''),
  ('Hannah', 'Montana',' Mountain 21', 'some long string3','', ''),
  ('Michael', 'Corse', 'Valley 345', 'some long string4','', '' ),
  ('Sandy', 'Mandy', 'Ocean blvd 2', 'some long string5','', ''),
  ('Betty', 'Bet', 'Green Grass 1', 'some long string6','', ''),
  ('Richard', 'Rich', 'Sky st 331', 'some long string7','', ''),

]
mycursor.execute("truncate table suspects")
mycursor.executemany(sql, val)

mydb.commit()