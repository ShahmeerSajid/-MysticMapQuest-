# MysticMapQuest: Your Epic (and Slightly Ridiculous) Treasure Hunt!
Ahoy, adventurer! Welcome to MysticMapQuest, the game where you’re a treasure-hunting, map-decoding mastermind (or at least you pretend to be). Armed with nothing but a cryptic 2D map, a few arrows, and sheer determination, you’ll embark on a journey to collect shiny treasures while trying not to trip over your own breadcrumbs. Sound easy? Well, it’s not. But it’s definitely fun!

"What’s the Game About?"
In MysticMapQuest, your mission—should you choose to accept it—is to navigate a randomly generated map full of twists, turns, and treasures (+). You’ll use simple directional symbols (<, >, v, ^) to move through the map, collecting treasures while leaving behind breadcrumbs (X) to mark where you’ve been. But beware: once you’ve marked a spot, there’s no going back… unless you like running in circles!

"Features That Make You Go "Arrr!" "
Map Magic: Create Your Own Treasure Map
Every good treasure hunt needs a map, right? With generate_treasure_map_row(width, boolean), you’ll be crafting rows of symbols that could lead to treasure—or just another dead end. Will it be a left turn? A right turn? A 3D vertical leap? Who knows? That’s half the fun!

"Follow the Breadcrumbs (But Don’t Get Lost)"
Once your map’s ready, it’s time to follow the trail with follow_trail(map_string, start_row, start_col, steps). This handy function helps you move through the map, collect those precious treasures, and avoid stepping on your own breadcrumbs. Think of it as your personal GPS for treasure hunting, but way more entertaining.

"Go 3D-ish with Your Map"
Why stick to boring 2D when you can add a dash of 3D? print_3D_treasure_map(map_string, width, height, depth) gives your map a little extra flair, turning your treasure quest into a multidimensional adventure. Sure, it’s still ASCII art, but it’s the coolest ASCII art around.

"Treasure Tally: Count Your Spoils"
After navigating the perilous map, it’s time to see what you’ve collected. count_treasures_and_symbols_visited(map_string) sums up your hard-earned treasures and counts the symbols you’ve visited. Will you walk away a wealthy adventurer or just another wannabe pirate with a penchant for getting lost?

"How to Play (Like a Pro)"
- Generate Your Map: Start by conjuring up a map filled with all sorts of mysterious symbols.
- Navigate the Maze: Use arrows to move through the map, grab treasures, and try not to retrace your steps.
- Celebrate Your Victory: Count your loot and symbols visited, and see if you’ve outsmarted the map—or if it outsmarted you.

"Why You’ll Love MysticMapQuest?"
- Every Map’s a New Adventure: Thanks to random map generation, no two games are the same.
- Challenge Yourself: Collect all the treasures without getting hopelessly lost.
- Retro Fun: Enjoy the simplicity of ASCII art and the thrill of exploration.

So grab your imaginary cutlass, don your best pirate accent, and dive into MysticMapQuest! It’s time to find out if you’re a true treasure hunter… or just another map-addicted adventurer :)

