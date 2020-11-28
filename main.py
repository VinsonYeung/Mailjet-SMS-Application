import requests
from tkinter import *
from tkinter import filedialog


if __name__ == "__main__":
    contact_info = []
    root = Tk()
    root.title("Send SMS")
    root.geometry("640x400")

    # Top frame
    topFrame = Frame(root)
    topFrame.pack(side=TOP)
    bearer = Entry(topFrame, width=640)
    bearer.insert(END, 'Insert Bearer Token')
    bearer.pack(side=TOP)
    select = Button(topFrame, text='Select .csv file', fg='black', command=lambda: select_file())
    select.pack(side=LEFT)
    send = Button(topFrame, text='Send messages', fg='black', command=lambda: send_messages())
    send.pack(side=RIGHT)
    sendCounter = Label(topFrame, text="Successful: - Failed: ")
    sendCounter.pack(side=BOTTOM)

    # Center frame
    centerFrame = Frame(root)
    centerFrame.pack(side=TOP)
    fileName = Label(centerFrame, text="No file")
    fileName.pack(side=TOP)
    fromName = Entry(centerFrame, width=640)
    fromName.insert(END, 'SMS sender name')
    fromName.pack(side=BOTTOM)

    # Bottom frame
    bottomFrame = Frame(root, height=300)
    bottomFrame.pack(side=BOTTOM)
    contactDisplay = Listbox(bottomFrame, width=640, height=200, selectmode=BROWSE, fg='black')
    contactDisplay.pack(side=TOP)

    # Opens a menu to select a .csv file
    def select_file():
        file = filedialog.askopenfile(mode='r', filetypes=[('csv files', '*.csv')])
        # Reset send attempt counter
        sendCounter['text'] = "Successful: - Failed: "
        # No file selected
        if file is None:
            fileName['text'] = "No file"
            contact_info.clear()
            contactDisplay.delete(0, END)
        else:
            content = file.read()
            fileName['text'] = file.name
            contact_info.clear()
            contactDisplay.delete(0, END)

            lines = content.split('\n')
            for l in lines:
                column = l.split(',')
                contact_info.append(column)
                contactDisplay.insert(END, l)

    # Send sms messages according to the information in the .csv file
    def send_messages():
        successful_sends = 0
        failed_sends = 0
        message_count = 0
        messages = contactDisplay.get(0, END)
        # Write .csv of status codes
        f = open("log.csv", "w")

        for m in contact_info:
            url = "https://api.mailjet.com/v4/sms-send"

            payload = "{\n    \"Text\": \"" + m[3] + "\",\n    \"To\": \"" + m[2] + "\",\n    \"From\": \"" + \
                      fromName.get() + "\"\n}"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + bearer.get()
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            # Count failed sends
            if response.ok:
                successful_sends += 1
            else:
                failed_sends += 1
                f.write(messages[message_count] + "\n")

            message_count += 1

        sendCounter['text'] = "Successful: " + str(successful_sends) + " - Failed: " + str(failed_sends)
        f.close()

    mainloop()
