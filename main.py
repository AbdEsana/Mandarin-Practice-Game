import pygame
import random
from bidi.algorithm import get_display  # Import BiDi algorithm

# Initialize Pygame
pygame.init()
selected_level = None  # Initially, no level is selected
# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Symbol Translation Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Fonts
symbol_font = pygame.font.Font("NotoSerifSC-Regular.otf", 36)  # Font for Mandarin symbols
pinyin_font = pygame.font.Font("NotoSerifSC-Regular.otf", 24)  # Font for Pinyin
translation_font = pygame.font.Font("OpenSans-Regular.ttf", 28)  # Font for translations

# trans buttons
trans_button_width = 400  # Increase button width
trans_button_height = 50
trans_button_spacing = 20

# List of words, each containing [symbol, pinyin, translation]
words = [
    [["我", "wǒ"], "אני"],
    [["你", "nǐ"], "את/אתה"],
    [["他", "tā"], "הוא"],
    [["她", "tā"], "היא"],
    [["您", "nín"], "אתה /את בכבוד"],
    [["好", "hǎo"], "טוב, נחמד, בסדר"],
    [["高兴", "gāoxìng"], "שמח"],
    [["忙", "máng"], "עסוק"],
    [["困", "kùn"], "ישנוני"],
    [["渴", "kě"], "צמא"],
    [["饿", "è"], "רעב"],
    [["累", "lèi"], "עייף"],
    [["早", "zǎo"], "מוקדם"],
    [["晚", "wǎn"], "מאוחר"],
    [["好吃", "hǎochī"], "טעים לאוכל"],
    [["好喝", "hǎohē"], "טעים לשתיה"],
    [["大", "dà"], " גדול"],
    [["小", " xiǎo"], "קטן"],
    [["漂亮", "piàoliang"], "יפה"],
    [["美", "měi"], "יפה"],
    [["好看", "hǎokàn"], "יפה"],
    [["帅", "shuài"], "חתיך"],
    [["多", "duō"], "הרבה"],
    [["对", "duì"], "נכון"],
    [["少", "shǎo"], "מועט"],
    [["喜欢", "xǐhuan"], "לאהוב"],
    [["叫", "jiào"], "להקרא בשם"],
    [["请", "qǐng"], "לבקש ,להזמין"],
    [["问", "wèn"], "לשאול"],
    [["姓", "xìng"], "שם משפחה"],
    [["认识", "rènshi"], "להכיר"],
    [["在", "zài"], "נמצא"],
    [["进", "jìn"], "להכנס"],
    [["坐", "zuò"], "לשבת"],
    [["谢谢", "xièxie"], "תודה"],
    [["是", "shì"], "to be הפועל"],
    [["学习", "xuéxí"], "ללמוד"],
    [["学", "xué"], "ללמוד"],
    [["吃饭", "chīfàn"], "לאכול"],
    [["喝", "hē"], "לשתות"],
    [["看", "kàn"], "להסתכל"],
    [["要", "yào"], "רוצה, צריך"],
    [["有", "yǒu"], "יש"],
    [["没有", "méiyǒu"], "אין"],
    [["工作", "gōngzuò"], "לעבוד, עבודה"],
    [["做", "zuò"], "לעשות, להכין"],
    [["去", "qù"], "ללכת, לנסוע"],
    [["差", "chà"], "חסר"],
    [["回", "huí"], "לחזור"],
    [["来", "lái"], "לבוא"],
    [["上课", "shàng kè"], "להתחיל שיעור"],
    [["下课", "xià kè"], "לסיים שיעור"],
    [["休息", "xiūxi"], "לנוח"],
    [["名字", "míngzì"], "שם"],
    [["姓", "xìng"], "שם משפחה"],
    [["谢谢", "xièxie"], "תודה"],
    [["老师", "lǎoshī"], "מורה"],
    [["朋友", "péngyou"], "חבר"],
    [["男朋友", "nán péngyou"], "חבר"],
    [["女朋友", "nǚ péngyou"], "חברה"],
    [["女", "nǚ"], "female"],
    [["男", "nán"], "male"],
    [["同学", "tóngxué"], "חבר לכיתה"],
    [["人", "rén"], "איש, אדם"],
    [["点心", "diǎnxīn"], "חטיפים"],
    [["爸爸", "bàba"], "אבא"],
    [["妈妈", "māma"], "אמא"],
    [["哥哥", "gēge"], "אח גדול"],
    [["姐姐", "jiějie"], "אחות גדולה"],
    [["妹妹", "mèimei"], "אחות צעירה"],
    [["弟弟", "dìdi"], "אח צעיר"],
    [["女儿", "nǚ ér"], "בת"],
    [["儿", "érzi"], "בן"],
    [["孩子", "háiz"], "ילד/ים"],
    [["米饭", "mǐfàn"], "אורז מבושל"],
    [["米", "mǐ"], "אורז גולמי"],
    [["饭", "fàn"], "ארוחה, אוכל"],
    [["面条", "miàntiáo"], "נודלס"],
    [["饺子", "jiǎozi"], "כיסונים"],
    [["包子", "bāozi"], "באודזה"],
    [["面包", "miànbāo"], "לחם"],
    [["汉堡包", "hànbǎobāo"], "המבורגר"],
    [["比萨饼", "bǐsàbǐng"], "פיצה"],
    [["巧克力", "qiǎokèlì"], "שוקולד"],
    [["家", "jiā"], "משפחה / בית"],
    [["照片", "zhàopiàn"], "תמונה"],
    [["工作", "gōngzuò"], "עבודה"],
    [["医生", "yīshēng"], "רופא"],
    [["狗", "gǒu"], "כלב"],
    [["课", "kè"], "שיעור"],
    [["今年", "jīnnián"], "השנה"],
    [["年", "nián"], "שנה"],
    [["今天", "jīntiān"], "היום"],
    [["天", "tiān"], "יום"],
    [["经理", "jīnglǐ"], "מנהל"],
    [["学生", "xuésheng"], "סטודנט ,תלמיד"],
    [["先生", "xiānsheng"], "מר, בעל"],
    [["太太", "tàitai"], "גברת"],
    [["早饭", "zǎofàn"], "ארוחת בוקר"],
    [["午饭", "wǔfàn"], "ארוחת צהריים"],
    [["晚饭", "wǎnfàn"], "ארוחת ערב"],
    [["中国", "Zhōngguó"], "סין"],
    [["以色列", "Yǐsèliè"], "ישראל"],
    [["日本", "Rìběn"], "יפן"],
    [["汉语", "Hànyǔ"], "סינית"],
    [["英国", "Yīngguó"], "אנגליה"],
    [["美国", "Měiguó"], "ארהב"],
    [["俄国", "éguó"], "רוסיה"],
    [["法国", "Fǎguó"], "צרפת"],
    [["加拿大", "Jiānádà"], "קנדה"],
    [["德国", "Déguó"], "גרמניה"],
    [["希伯来语", "Xībóláiyǔ"], "עברית"],
    [["日语", "Rìyǔ"], "יפנית"],
    [["英语", "Yīngyǔ"], "אנגלית"],
    [["俄语", "éyǔ"], "רוסית"],
    [["法语", "Fǎyǔ"], "צרפתית"],
    [["德语", "Déyǔ"], "גרמנית"],
    [["阿拉伯语", "ālābóyǔ"], "ערבית"],
    [["很", "hěn"], "מאד"],
    [["也", "yě"], "גם"],
    [["最近", "zuìjìn"], "לאחרונה"],
    [["最", "zuì"], "הכי"],
    [["不", "bù"], "לא"],
    [["太", "tài"], "מאד, יותר מדי"],
    [["不太", "bú tài"], "לא כל כך"],
    [["刚", "gāng"], "הרגע"],
    [["都", "dōu"], "כל / שניהם"],
    [["一共", "yígòng"], "בסך הכל"],
    [["还", "hái"], "בנוסף"],
    [["真", "zhēn"], "באמת"],
    [["什么", "shénme"], "מה?"],
    [["吗", "ma"], "האם"],
    [["怎么样", "zěnmeyàng"], "איך"],
    [["呢", "ne"], "מה לגבי"],
    [["贵姓", "guìxìng"], "מה שם משפתך"],
    [["哪国人", "nǎ guó rén"], "בן איזו ארץ"],
    [["几", "jǐ"], "כמה"],
    [["谁", "shéi"], "מי, את מי, למי"],
    [["多少", "duōshao"], "כמה"],
    [["哪", "nǎ"], "איזה"],
    [["口", "kǒu"], "מילת מדידה לנפשות"],
    [["个", "ge"], "מילת מדידה כללית"],
    [["张", "zhāng"], "מדידה עצמים שטוחים"],
    [["只", "zhī"], "מדידה לכלבים"],
    [["条", "tiáo"], "מדידה לדברים ארוכים"],
    [["岁", "suì"], "שנת גיל"],
    [["杯", "bēi"], "כוס"],
    [["点", "diǎn"], "מדידה לשעה"],
    [["刻", "kè"], "רבע שעה"],
    [["分", "fēn"], "דקה / דקות"],
    [["零", "líng"], "אפס"],
    [["一", "yī"], "אחת"],
    [["二", "èr"], "שתיים"],
    [["两", "liǎng"], "שני / שתי"],
    [["三", "sān"], "שלוש"],
    [["四", "sì"], "ארבע"],
    [["五", "wǔ"], "חמש"],
    [["六", "liù"], "שש"],
    [["七", "qī"], "שבע"],
    [["八", "bā"], "שמונה"],
    [["九", "jiǔ"], "תשע"],
    [["十", "shí"], "עשר"],
    [["九十九", "jiǔ shí jiǔ"], "99"],
    [["半", "bàn"], "חצי"],
    [["茶", "chá"], "תה"],
    [["咖啡", "kāfēi"], "קפה"],
    [["酒", "jiǔ"], "יין"],
    [["水", "shuǐ"], "מים"],
    [["可乐", "kělè"], "קולה"],
    [["豆浆", "dòujiāng"], "חלב סויה"],
    [["牛奶", "niúnǎi"], "חלב"],
    [["橙汁", "chéngzhī"], "מיץ תפוזים"],
    [["早上", "zǎoshang"], "בוקר"],
    [["晚上", "wǎnshang"], "ערב"],
    [["明天", "míngtiān"], "מחר"],
    [["上午", "shàngwǔ"], "לפני הצהריים"],
    [["下午", "xiàwǔ"], "אחר הצהריים"],
    [["现在", "xiànzài"], "עכשיו"],
    [["今天", "jīntiān"], "היום"],
    [["今年", "jīnnián"], "השנה"],
    [["请问", "qǐngwèn"], "סליחה"],
    [["还行", "hái xíng"], "לא רע"],
    [["马马虎虎", "mǎmǎhūhū"], "ככה ככה"],
    [["对不起", "duìbuqǐ"], "סליחה"],
    [["这", "zhè"], "זה"],
    [["那", "nà"], "ההוא"],
    [["再见", "zàijiàn"], "להתראות"],
    [["的", "de"], "מציין שייכות"],
    [["和", "hé"], "ו"],
    [["几", "ji"], "אחדים ,כמה"],

    # Add more words as needed
]


# Function to display text on the screen with the specified font
def display_text(text, x, y, color=BLACK, font=None):
    if font is None:
        font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    text_rect.y = y
    screen.blit(text_surface, text_rect)


# Function to display buttons for translations
def display_translation_buttons(translations, correctTrans):
    correctIndex = -1
    x = 200  # Adjust x-coordinate for centering buttons
    y = 300

    # Shuffle the translations list to randomize the order
    random.shuffle(translations)
    # Display buttons for return l
    levelreturn_button_rect = pygame.Rect(600, 300 + ((trans_button_height + trans_button_spacing) * 3),
                                          (trans_button_width // 2), trans_button_height)
    pygame.draw.rect(screen, GREEN, levelreturn_button_rect)
    display_text("return", 650, 300 + ((trans_button_height + trans_button_spacing) * 3) + 10,
                 color=WHITE)  # Change text color to black

    # Use the translation_font for rendering the translations
    for i, translation in enumerate(translations):
        if translation == correctTrans:
            correctIndex = i
        button_rect = pygame.Rect(x, y + (trans_button_height + trans_button_spacing) * i, trans_button_width,
                                  trans_button_height)
        pygame.draw.rect(screen, GREEN, button_rect)
        bidi_translation = get_display(translation)  # Apply BiDi algorithm
        text_surface = translation_font.render(bidi_translation, True, WHITE)  # Render text surface
        text_rect = text_surface.get_rect(center=button_rect.center)  # Get rect with center aligned
        screen.blit(text_surface, text_rect)  # Blit text onto button


    return correctIndex


# Function to display the menu screen
def show_menu():
    screen.fill(WHITE)
    # Load a Chinese font
    chinese_font = pygame.font.Font("NotoSerifSC-Regular.otf", 36)

    # Display title
    title_text = chinese_font.render("Word Game", True, GREEN)  # "Word Game" in Chinese Mandarin
    title_rect = title_text.get_rect(center=(screen_width // 2, 50))
    screen.blit(title_text, title_rect)

    # Display buttons for each level
    level1_button_rect = pygame.Rect(100, 100, 200, 50)
    pygame.draw.rect(screen, GREEN, level1_button_rect)
    display_text("Level 1", 130, 115, color=WHITE)  # Change text color to black

    level2_button_rect = pygame.Rect(100, 200, 200, 50)
    pygame.draw.rect(screen, GREEN, level2_button_rect)
    display_text("Level 2", 130, 215, color=WHITE)  # Change text color to black

    level3_button_rect = pygame.Rect(100, 300, 200, 50)
    pygame.draw.rect(screen, GREEN, level3_button_rect)
    display_text("Level 3", 130, 315, color=WHITE)  # Change text color to black

    pygame.display.flip()  # Update the display


# Function to start the game
# Function to start the game
def start_game(level):
    score = 0
    running = True
    words_copy = list(words)  # Make a copy of the words list to modify for different levels

    while running:
        screen.fill(WHITE)

        # Display the word elements based on the level
        if level == 1:
            current_word = random.choice(words_copy)
            word_info, correct_translation = current_word
            display_text("Symbol: " + word_info[0], 100, 100, font=symbol_font,
                         color=BLACK)  # Change text color to black
            display_text("Pinyin: " + word_info[1], 100, 200, font=pinyin_font,
                         color=BLACK)  # Change text color to black
            translations = [correct_translation] + random.sample(
                [word[1] for word in words_copy if word[1] != correct_translation], 2)
        elif level == 2:
            current_word = random.choice(words_copy)
            word_info, correct_translation = current_word
            display_text("Pinyin: " + word_info[1], 100, 100, font=pinyin_font,
                         color=BLACK)  # Change text color to black
            translations = [correct_translation] + random.sample(
                [word[1] for word in words_copy if word[1] != correct_translation], 2)
        elif level == 3:
            current_word = random.choice(words_copy)
            word_info, correct_translation = current_word
            display_text("Symbol: " + word_info[0], 100, 100, font=symbol_font,
                         color=BLACK)  # Change text color to black
            translations = [correct_translation] + random.sample(
                [word[1] for word in words_copy if word[1] != correct_translation], 2)

        # Display buttons for translations
        correctButtonIndex = display_translation_buttons(translations, correct_translation)


        # Display score
        display_text("Score: " + str(score), 600, 50, color=BLACK)  # Change text color to black

        pygame.display.flip()  # Update the display

        answer_clicked = False

        while not answer_clicked:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    answer_clicked = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if any button is clicked
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    choice = clickedButton(mouse_x, mouse_y)
                    if choice == correctButtonIndex:
                        score += 1
                        answer_clicked = True
                    elif choice == -2:
                        return score, False
                    elif choice != -1:
                        return score, True

        pygame.time.wait(200)  # Wait for 0.6 second before updating the screen and randomizing again

    pygame.quit()

def clickedButton(mouse_x, mouse_y):
    for i in range(3):
        if 200 <= mouse_x <= 200 + trans_button_width and 300 + (
                trans_button_height + trans_button_spacing) * i <= mouse_y <= 300 + trans_button_height + (
                trans_button_height + trans_button_spacing) * i:
            return i
        if 600 <= mouse_x <= 600 + trans_button_width//2 and 300 + (
                trans_button_height + trans_button_spacing) * 3 <= mouse_y <= 300 + trans_button_height + (
                trans_button_height + trans_button_spacing) * 3:
            return -2
    return -1

def show_gameover(score):
    global isOver
    screen.fill((255, 0, 0))  # Fill the screen with red color

    # Display game over message
    gameover_font = pygame.font.Font(None, 50)
    gameover_text = gameover_font.render("Game Over", True, BLACK)
    gameover_rect = gameover_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    screen.blit(gameover_text, gameover_rect)

    # Display score
    score_text = gameover_font.render("Score: " + str(score), True, BLACK)
    score_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(score_text, score_rect)

    # Display return button
    return_button_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)
    pygame.draw.rect(screen, BLACK, return_button_rect)
    display_text("Return", screen_width // 2 - 45, screen_height // 2 + 65, color=WHITE)

    pygame.display.flip()

    answer_clicked = False

    while not answer_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                answer_clicked = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if any button is clicked
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if screen_width // 2 - 100<=mouse_x<=screen_width // 2 + 100 and screen_height // 2 + 50<=mouse_y<=screen_height // 2 + 100:
                    return

    pygame.time.wait(200)  # Wait for 0.6 second before updating the screen and randomizing again

# Main function
def main():
    show_menu()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if any button on the menu is clicked
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 100 <= mouse_x <= 300 and 100 <= mouse_y <= 150:
                    selected_level = 1
                elif 100 <= mouse_x <= 300 and 200 <= mouse_y <= 250:
                    selected_level = 2
                elif 100 <= mouse_x <= 300 and 300 <= mouse_y <= 350:
                    selected_level = 3
                # Start the game with the selected level
                if selected_level is not None:
                    score, isOver = start_game(selected_level)
                    if isOver:
                        show_gameover(score)
                    selected_level = None
                    show_menu()

    pygame.quit()


if __name__ == "__main__":
    main()
