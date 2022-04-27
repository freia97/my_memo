import os

simvol = ""
count = None
res = ""
with open("count.txt", "r") as file:
    content = file.read()
    count = int(content)

def addNote():
    print("введите текст новой заметки, после ввода нажмите ввод")
    note = input()
    with open("notes/note_" + str(count) + ".txt", "w") as file:
        file.write(note)
    print("заметка создана!")

def openNote():
    print("всего заметок-", count - 1)
    print("введите номер заметки, которую хотите открыть")
    num = input()
    with open("notes/note_" + num + ".txt", "r") as file:
        res = file.read()
        print(res)

def updateNote():
    print("всего заметок-", count - 1)
    print("введите номер заметки, которую хотите дополнить")
    num = input()
    with open("notes/note_" + num + ".txt", "a") as file:
        print("введите текст, который хотите добавить, после ввода нажмите ввод")
        note = input()
        file.write(note)
        print("заметка обновлена!")

def delNote():
    print("всего заметок-", count - 1)
    print("введите номер заметки для удаления")
    num = input()
    path = os.path.join("notes/note_" + num + ".txt")
    os.remove(path)
    print("заметка успешно удалена!")

while True:
    print("создать заметку нажмите- a, открыть заметку-"
          "нажмите- o, обновить заметку нажмите- u"
          "удалить заметку нажмите- d")
    simvol = input()
    if simvol == "a":
        addNote()
        count += 1
    elif simvol == "o":
        openNote()
    elif simvol == "u":
        updateNote()
    elif simvol == "d":
        delNote()
        count -= 1
        # dirPath = "notes"
        # result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
        # print(result)
        # for i in range(0, count):
        #     old_file = os.path.join("notes" + result[i])
        #     new_file = os.path.join("notes/note_" + str(count))
        #     os.rename(old_file, new_file)


    with open("count.txt", "w") as file:
        file.write(str(count))