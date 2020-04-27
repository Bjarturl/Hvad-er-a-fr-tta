
import pyodbc
def writeToFiles():
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=DESKTOP-LDAOU7M\\SQLEXPRESS;"
                          "Database=PersonalProjects;"
                          "Trusted_Connection=yes;")
    cursor = cnxn.cursor()
    cursor.execute("SELECT A.Title, A.ImageCaption, A.article FROM AllNewsArticles A")

    f1 = open('titles.txt', "w+") #open with write permission to clear file
    f1.close()
    f1 = open('articles.txt', "w+") #open with write permission to clear file
    f1.close()
    f1 = open('captions.txt', "w+") #open with write permission to clear file
    f1.close()
    f1 = open('images.txt', "w+") #open with write permission to clear file
    f1.close()
    for row in cursor:
        article = row[-1]
        title = row[0]
        caption = row[1]
        try:
            if article != "" and title != "" and caption != "":
                with open("titles.txt", 'a', encoding="utf-8") as f1:
                    f1.write(title + "\n")
                with open("articles.txt", 'a', encoding="utf-8") as f1:
                    f1.write(article + "\n")
                with open("captions.txt", 'a', encoding="utf-8") as f1:
                    f1.write(caption + "\n")
        except:
            pass

    imgs = cnxn.cursor() 
    imgs.execute("SELECT A.NewsImageLink FROM AllNewsArticles A")
    with open("images.txt", 'a', encoding="utf-8") as f1:
        for row in imgs:
            if row[0] != "" and row[0] != None:
                f1.write(row[0])
                f1.write("\n")
#writeToFiles()
