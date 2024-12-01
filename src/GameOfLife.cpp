#include "GameOfLife.h"
#include <algorithm>


gl::GameOfLife::GameOfLife() {
	this->current_grid = new bool[gl::GRID_SIZE];
	this->next_grid = new bool[gl::GRID_SIZE];	
	this->reset();
}


gl::GameOfLife::~GameOfLife() {
	delete[] this->current_grid;
	delete[] this->next_grid;
}


void gl::GameOfLife::start() {
	this->is_running = true;
}


void gl::GameOfLife::pause() {
	this->is_running = !this->is_running;
}


void gl::GameOfLife::reset() {
	bool* begin = this->current_grid;
	bool* end = this->current_grid + gl::GRID_SIZE;
	for (bool* p = begin; p < end; p++)
		*p = false;
}


void gl::GameOfLife::random_grid() {
	bool* begin = this->current_grid;
	bool* end = this->current_grid + gl::GRID_SIZE;
	for (bool* p = begin; p < end; p++)
		*p = GetRandomValue(1, 10) <= 2;
}


int gl::GameOfLife::count_neighbors(const int n) {
	int c = 0;	
	c += n - 1 >= 0 && this->current_grid[n - 1];
	c += n + 1 < gl::GRID_SIZE && this->current_grid[n + 1];
	
	c += n - gl::GRID_COLS >= 0 && this->current_grid[n - gl::GRID_COLS];
	c += n + gl::GRID_COLS < gl::GRID_SIZE && this->current_grid[n + gl::GRID_COLS];

	c += n + gl::GRID_COLS + 1 < gl::GRID_SIZE && this->current_grid[n + gl::GRID_COLS + 1];
	c += n + gl::GRID_COLS - 1 < gl::GRID_SIZE && this->current_grid[n + gl::GRID_COLS - 1];

	c += n - gl::GRID_COLS + 1 >= 0 && this->current_grid[n - gl::GRID_COLS + 1];
	c += n - gl::GRID_COLS - 1 >= 0 && this->current_grid[n - gl::GRID_COLS - 1];
	return c;
}


void gl::GameOfLife::update() {
	if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON)) {
		const Vector2 m_pos = GetMousePosition();
		const int r = m_pos.y / gl::CELL_SIZE;
		const int c = m_pos.x / gl::CELL_SIZE;
		const int n_cell = r * gl::GRID_COLS + c;		
		this->current_grid[n_cell] = !this->current_grid[n_cell];
	}

	if (this->is_running == false) {
		return;
	}

	for (int i = 0; i < gl::GRID_SIZE; i++) {
		const bool state = this->current_grid[i];
		const int n_neighbors = this->count_neighbors(i);		
		this->next_grid[i] = (
			(state == false && n_neighbors == 3) || 
			(state == true && n_neighbors == 2 || n_neighbors == 3)
		);
	}	
}


void gl::GameOfLife::draw() {
	for (int i = 0; i < gl::GRID_ROWS; i++) {
		for (int j = 0; j < gl::GRID_COLS; j++) {			
			if (this->current_grid[i * gl::GRID_COLS + j] == true) {
				DrawRectangle(
					j * gl::CELL_SIZE, 
					i * gl::CELL_SIZE, 
					gl::CELL_SIZE, 
					gl::CELL_SIZE, 
					gl::CELL_COLOR
				);
			}
		}
	}
	if (this->is_running) {
		std::swap(this->current_grid, this->next_grid);
	}
}
