def checkVowel(n):
    match n:
        case 'a': return "This is a vowel"
        case 'e': return "This is a vowel"
        case 'i': return "This is a vowel"
        case 'o': return "This is a vowel"
        case 'u': return "This is a vowel"
        case _: return "This is a consonant"
        
print(checkVowel('a'))
print(checkVowel('z'))
print(checkVowel('f'))
print(checkVowel('i'))