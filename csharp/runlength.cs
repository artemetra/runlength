using System;

class Program {
    static void Main(string[] args) {
        // вот на этом месте можно вписывать любые буквы в код
        string text = "bbbbbbbbbrrrrrruuuuhhh";
        int Count = 0;
        char PreCh = '\\';
        foreach (char ch in text)
        {
           foreach (char cha in text) {
              if (cha != PreCh && cha == ch) {
                 Count++;
              }
           }
           if (Count != 0) {
              Console.WriteLine("Количество символов {0} = {1}", ch, Count);
           Count = 0;
           PreCh = ch;
           }
        }
        Console.ReadKey();
    }
}
