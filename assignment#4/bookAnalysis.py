#Emma Collins


def analyzeBook(filename):
    count = {}
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                word = word.replace('_', '').replace('"', '').replace(',','').replace('.','')
                word = word.replace('-', '').replace('?', '').replace('!','').replace("'","")
                word = word.replace('(', '').replace(')', '').replace(':','').replace("[",'')
                word = word.replace(']', '').replace(';','')

                word = word.lower()

                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word]= 1
    return count

def outputAnalysis(count, title):
    try:
        keys = list(count.keys())
        keys.sort()
        output_filename = f"{title}_analysis.txt"
        with open(output_filename, 'w') as out:
            for word in keys:
                out.write(f"{word} {str(count[word])}\n")
        return True
    except Exception as e:
        print(f"Error writing analysis to file: {e}")
        return False
    
def main():
    book_filename = 'chemWar.txt'
    title = book_filename.rsplit('.',1)[0]
    count = analyzeBook(book_filename)

    success = outputAnalysis(count, title)
    if success:
        print(f"Analysis saved to {title}_analysis.txt")
    else:
        print("Analysis failed to save")

if __name__=="__main__":
    main()

