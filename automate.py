from PIL import Image, ImageDraw, ImageFont
import textwrap

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)

# Text
FONT = "font/CONSOLA.ttf"
WIDTH = 1000  # in px
HEIGHT = 250  # in px

# Size
FONT_SIZE = 50  # in px

# Style
TEXT_COLOR = WHITE  # in rgb
STROKE_COLOR = BLACK  # in rgb
THICC_NESS = 3  # in px

# Background
BACKGROUND_COLOR = GRAY  # in rgb
BACKGROUND_OPACITY = 0
WIDTH_MARGIN = 0
HEIGHT_MARGIN = 0

SCRIPT = [
    "Pa, pwede po bang makahingi ng limang piso?",
    "teka lang nak...",
    "Natapos na namang muli ang isang termino",
    "Ano ang nabago? Ano ang nadagdag?",
    "Ano ang nawala? Sino ang nanatili?",
    "Sino ang sumuko?",
    "Hwag kasi kayong umasa sa gobyerno!",
    "Kayo pa rin ang nagtatrabaho",
    "Magsikap kayo para maging maayos ang mga buhay nyo!",
    "Tunay ngang ang kamangmangan ay tila ba ginawang sandata ng karamihan",
    "Sa mga taong naluklok sa gobyerno",
    "Waring naging lason sa isip na unti-unting pumapatay sa ating inang bayan.",
    "Umasa? Masayang tumanggap ng tulong.",
    "Lalo na kung walang hinihintay na kapalit at totoong bukal sa puso,",
    "Hinding hindi namin mapepeke at maaalis ang ngiti ng pasasalamat namin.",
    "Ngunit ang umasa kami?",
    "Hindi kami ganoon, araw gabing kaming walang reklamo sa pag-aararo",
    "Sinasabayan ng alon ang aming pangambang dala ng dagat",
    "Hindi kami nagpapatinag sa antok",
    "tuwing binabaybay ang kalsada sa kahit anong oras pa",
    "Sinasabayan naming gumising ang mga manok",
    "para lamang makahanap ng aming pangkain at pangtustoa.",
    "Kami ay kumikilos at humihingi ng asistansya sa nararapat.",
    "Hindi kami basta basta umaasa.",
    "Hindi. Hindi kami umaasa.",
    "Ayan! D'yan kayo nagsisilabasan! Sa eleksyon! Dyan kayo mabait palagi!",
    "Halalan na naman, sana naman maayos na ang susunod na mamumuno",
    "Nak! Pakibasa mo nga ito sa akin!",
    "Wala tay! Tungkol na naman sa eleksyon!",
    "Basahin mo nga yan sa akin!",
    "Magaling mamalatkayo ang midya, mahirap usisain ang totoo at hindi.",
    "Nagsisikilos kayo sa harap ng midya",
    "na para bang ginawa nyo na",
    "ang lahat ang inyong makakaya.",
    "Sino ba talaga ang may pagkukulang?",
    "Masasabi ba nating kulang pa ang kalyo, sugat, pawis at dugo",
    "na aming inilalahad upang may mahanap na piso sa bawat araw?",
    "Ano ba ang aming kakulangan at bakit tila ba hindi namin maabot at matalo",
    "ang sistemang naglilimita sa aming pagtanaw ng mas maayos na bukas?",
    "Kailan nyo ba balak itigil ang pagkupit",
    "sa bawat pirasong dapat ay bumubuo sa mga pangarap",
    "na nais naming iguhit?",
    "Saan nga ba kami nagkulang at kami ang nauubusan ng ani",
    "gayong kami ang nagbungkal at nagtanim ng mga ito?",
    "Kanino ba dapat isisi ang pakikipagkarera namin sa mamahaling kalsada?",
    "Paano ba namin maibibigay ang tamang bukas para sa aming pamilya?",
    "Pakiusap. Kailangan namin ng tunay na lider.",
    "Maayos at malinis na pamahalaan.",
    "Pamahalaang bibigyang pansin ang mahihinang sigaw namin!",
    "Gobyernong walang buwayang may matalas na kuko at mga ngipin,",
    "hindi pagbabalatkayo ang mga gawa nakaharap man o",
    "hindi sa bawat litratong laman dyaryo. Pakiusap.",
    "Itong pisong ito ang sumisimbolo sa atin mismong pagkatao",
    "Hindi lamang ito basta perang barya",
    "subalit isa itong patunay ng ating pagka-Pilipino.",
    "Kabataan nasa iyo ang pag-asa.",
    "Pumili ka ng pangulong sasamahan kang tupdin ang bansang maginhawa.",
]


def process(sentence, file_name):
    sentence = textwrap.wrap(sentence, width=30)

    font = ImageFont.truetype(FONT, FONT_SIZE)
    image = Image.new("RGBA", (WIDTH, HEIGHT), (255, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # font_width, font_height = font.getsize(sentence)
    # new_width = (WIDTH - font_width) / 2
    # new_height = (HEIGHT - font_height) / 2

    # draw.text(
    #     (new_width, new_height), sentence, font=font, fill=WHITE, align="center",
    #     stroke_width=THICC_NESS, stroke_fill=STROKE_COLOR
    # )

    current_height, pad = 50, 10

    for line in sentence:
        w, h = draw.textsize(line, font=font)
        xy = ((WIDTH - w) / 2, current_height)

        draw.text(
            xy, line, font=font, fill=WHITE, align='center', stroke_width=THICC_NESS,
            stroke_fill=STROKE_COLOR
        )

        current_height += h + pad

    image.save(file_name)
    print(f'processed {file_name}')


def main():
    for index, sentence in enumerate(SCRIPT):
        process(
            sentence,
            f"results/{index:02}.png"
        )


if __name__ == "__main__":
    main()
