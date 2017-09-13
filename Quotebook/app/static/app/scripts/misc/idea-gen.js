var nouns = [
    "app",
    "fish",
    "charity",
    "hat",
    "pair of glasses",
    "vegetable patch",
    "drug",
    "school",
    "snack",
    "book",
    "secret society",
    "television",
    "group of friends",
    "break room",
    "subcommittee on national parks",
    "pope",
    "wig",
    "coffee maker",
    "toaster",
    "floor joist",
    "left pinky toe",
    "crown",
    "genetic disease",
    "canned soup",
    "boat",
    "submarine",
    "sandwich"
    "species of bear"
    "famous writer",
    "economic system",
    "financial derivative"
    "artillery shell",
    "seafood special",
    "celebrity chef",
    "serial killer",
    "big red button",
    "beekeeper"
    "Shakespearean actor"
]

var actions = [
    "turns lead into gold",
    "ends world hunger",
    "parallel parks",
    "cures diabetes",
    "solves the square root of 2",
    "knows what The Rock is cooking",
    "juggles chainsaws",
    "makes people believe God is real",
    "makes people believe God isn't real",
    "makes people believe this whole God thing isn't that important",
    "fixes the elevator",
    "tells you if your fly's down",
    "disarms North Korea",
    "builds the wall",
    "charges your iPhone",
    "does the dishes",
    "makes America great again",
    "cooks dinner",
    "ruins dinner",
    "never forgets",
    "plants trees",
    "cures Ebola",
    "gives you Ebola",
    "wins rock paper scissors",
    "benches 250 pounds",
    "sells crack",
    "may cause nausea",
    "wins the game of thrones",
    "kills people with fire",
    "performs colonoscopies",
    "makes bank errors in your favor",
    "sinks your battleship",
    "is not valid in Quebec",
    "cleans toxic waste",
    "creates toxic waste",
    "wears a hat",
    "sends you to New Zealand",
    "sees dead people",
    "knows why kids love Cinnamon Toast Crunch",
    "doesn't know why kids love Cinnamon Toast Crunch",
    "wears socks with sandals",
    "writes stories about talking dogs",
    "tastes like chalk and black pepper",
    "is made of people",
    "may have contributed to the rise of fascism",
    "commits war crimes",
    "is cruel and unusual punishment",
    "leads a communist uprising",
    "bans high-capacity magazines",
    "can dunk from the free throw line",
]

function choose(choices) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
}

var noun_text;
var action_text;

function generate_idea() {
    noun_text.text(choose(nouns));
    action_text.text(choose(actions));
}

$(document).ready(function() {
    noun_text = $("#idea-noun");
    action_text = $("#idea-action");
    generate_idea(noun_text, action_text)
});
