# territory-game-prototyping
Prototyping territory based game concepts written in Python (for now).

# To Do
* Main Game Loop
  * Check if game setup needed
  * Check for victory or defeat
  * Increment turn counter
* Game Setup
  * Determine map size
* Map Builder
  * Terrain type
* Player Class
  * Defense strength
  * Attack strength

# Game Mechanics/Rules
* Player starts with one base tile on the map.
* Each turn, the player can place one of two types of tiles on the board. A defensive tile or an offensive tile.
* All tiles must be connected.
* A lineage of the same type of tile accumulates strength.
  * One defense tile equals a strength of one.
  * Three defense tiles connected to each other will have a strength of three.
* A tile that has all the same type of tile surrounding it becomes a super tile.
  * Super tiles are a multiplier for the strength of their lineage.
* Defense tiles can only defend.
* Attack tiles can only attack.
