#pragma once
#include <raylib.h>


namespace gl {


	// Window
	constexpr int SCREEN_W{ 1080 };
	constexpr int SCREEN_H{ 720 };
	constexpr Color BACKGROUND_COLOR{ 18, 18, 18, 255 };
	constexpr int FPS{ 120 };
	constexpr char WINDOW_TITLE[]{ "Game of Life" };

	// Grid
	constexpr int CELL_SIZE{ 1 };
	constexpr int GRID_ROWS{ SCREEN_H / CELL_SIZE };
	constexpr int GRID_COLS{ SCREEN_W / CELL_SIZE };
	constexpr int GRID_SIZE{ GRID_ROWS * GRID_COLS };
	constexpr Color CELL_COLOR{ LIME };
}