<?php

declare(strict_types=1);

class Position
{
    public $rowIndex;
    public $columnIndex;

    function __construct(int $rowIndex, int $columnIndex)
    {
        $this->rowIndex = $rowIndex;
        $this->columnIndex = $columnIndex;
    }

    function leftDiagonal(): int {
        return $this->rowIndex - $this->columnIndex;
    }

    function rightDiagonal(): int {
        return $this->rowIndex + $this->columnIndex;
    }

    function __toString(): string {
        return sprintf('Position (%d, %d)', $this->rowIndex, $this->columnIndex);
    }
}
