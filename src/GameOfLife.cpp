#include "GameOfLife.h"


gl::GameOfLife::GameOfLife() {
	this->gen = (bool*) calloc(gl::GRID_MAX_SIZE, sizeof(bool));
	this->next_gen = (bool*) calloc(gl::GRID_MAX_SIZE, sizeof(bool));
	this->reset();
}


gl::GameOfLife::~GameOfLife() {
	free(this->gen);
	free(this->next_gen);
}


void gl::GameOfLife::start() {
	this->is_running = true;
}


void gl::GameOfLife::pause() {
	this->is_running = !this->is_running;
}


void gl::GameOfLife::reset() {
	bool* begin = this->gen;
	bool* end = this->gen + this->grid_size;
	for (bool* p = begin; p < end; p++)
		*p = false;
}


void gl::GameOfLife::random_grid() {
	bool* begin = this->gen;
	bool* end = this->gen + this->grid_size;
	for (bool* p = begin; p < end; p++)
		*p = GetRandomValue(1, 10) <= 2;
}


void gl::GameOfLife::change_cell_size(const int delta) {		
	if (
		this->cell_size + delta < GRID_MIN_CELL_SIZE || 
		this->cell_size + delta > GRID_MAX_CELL_SIZE
	) {
		return;
	}	
	this->cell_size += delta;
	this->rows = gl::SCREEN_H / this->cell_size;
	this->cols = gl::SCREEN_W / this->cell_size;
	this->grid_size = this->rows * this->cols;
	this->random_grid();
}


int gl::GameOfLife::count_neighbors(const int n) {
	int c = 0;	
	c += n - 1 >= 0 && this->gen[n - 1];
	c += n + 1 < this->grid_size && this->gen[n + 1];
	
	c += n - this->cols >= 0 && this->gen[n - this->cols];
	c += n + this->cols < this->grid_size && this->gen[n + this->cols];

	c += n + this->cols + 1 < this->grid_size && this->gen[n + this->cols + 1];
	c += n + this->cols - 1 < this->grid_size && this->gen[n + this->cols - 1];

	c += n - this->cols + 1 >= 0 && this->gen[n - this->cols + 1];
	c += n - this->cols - 1 >= 0 && this->gen[n - this->cols - 1];
	return c;
}


void gl::GameOfLife::update() {
	if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON)) {
		const Vector2 m_pos = GetMousePosition();
		const int r = m_pos.y / this->cell_size;
		const int c = m_pos.x / this->cell_size;
		const int n_cell = r * this->cols + c;		
		this->gen[n_cell] = !this->gen[n_cell];
	}

	if (this->is_running == false) {
		return;
	}

	for (int i = 0; i < this->grid_size; i++) {
		const bool state = this->gen[i];
		const int n_neighbors = this->count_neighbors(i);		
		this->next_gen[i] = (
			(state == false && n_neighbors == 3) || 
			(state == true && n_neighbors == 2 || n_neighbors == 3)
		);
	}	
}


void gl::GameOfLife::draw() {
	for (int i = 0; i < this->rows; i++) {
		for (int j = 0; j < this->cols; j++) {			
			if (this->gen[i * this->cols + j] == true) {
				DrawRectangle(
					j * this->cell_size, 
					i * this->cell_size, 
					this->cell_size, 
					this->cell_size,
					gl::CELL_COLOR
				);
			}
		}
	}
	if (this->is_running) {
		std::swap(this->gen, this->next_gen);
	}
}


void gl::GameOfLife::print() {
	std::string imagepath = SCREENSHOOT_DIR "image-";
	Image image = GenImageColor(this->cols * this->cell_size, this->rows * this->cell_size, gl::BACKGROUND_COLOR);
	for (int i = 0; i < this->rows; i++) {
		for (int j = 0; j < this->cols; j++) {
			if (this->gen[i * this->cols + j] == true) {
				ImageDrawRectangle(
					&image,
					j * this->cell_size,
					i * this->cell_size,
					this->cell_size,
					this->cell_size,
					gl::CELL_COLOR
				);				
			}
		}
	}

	std::filesystem::create_directory(SCREENSHOOT_DIR);
	const std::filesystem::path png = ".png";
	int n = 0;

	for (const auto& p : std::filesystem::directory_iterator(SCREENSHOOT_DIR)) {
		if (p.path().extension() == png) {
			n++;
		}
	}

	imagepath += std::to_string(n);
	imagepath += ".png";

	ExportImage(image, imagepath.c_str());
	UnloadImage(image);
}