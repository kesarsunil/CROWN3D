CROWN — 3D CHESS

Open CROWN_3D_Chess.html in a modern web browser. No installation or internet needed.
Click a piece then a highlighted square. Drag to orbit; scroll to zoom.
Play locally with a friend or choose the casual computer (you play White).
The match controls appear below the board on mobile. Scroll outside the board.

Includes real 3D meshes, animated moves, knight hops and shattering captures.
Castling, en passant, promotion, check, checkmate, stalemate, undo and keyboard moves are supported.
Threefold repetition and the 50-move rule are automatically drawn rather than requiring a claim.
The computer is a casual opponent, not a rated engine. No online multiplayer or saved games.
Enter e2e4 in the keyboard move box; add q/r/b/n for promotion, e.g. a7a8q.
Reduced-motion preference shortens moves and disables shattering.

MODELS
models/complete_chess_set.glb: board and all 32 pieces.
models/chess_board.glb: board alone.
models/white_*.glb and black_*.glb: six individual piece types per color.
GLB files use metres and Y-up. Squares are 5 cm wide; king is approximately 11.6 cm tall.
Blender: File > Import > glTF 2.0. The supplied Python script imports the complete set and saves a .blend.
These are procedurally generated models inspired by your king photo, not exact scans or Blender-authored assets.
Capture fragments are a stylized visual effect, not a physical fracture simulation.
Geometry is for rendering, not guaranteed watertight for 3D printing.

SOURCE
The HTML contains all CSS, JavaScript and mesh definitions. Source files are also included.
Run node build.js to rebuild the standalone HTML and all GLBs. No packages required.
A WebGL-compatible browser is required; enable hardware acceleration if needed.
