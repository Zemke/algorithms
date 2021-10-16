<?php

declare(strict_types=1);

require_once('./Main.php');

class Test {

  private static function isSafeRook(array $positions, $rook) : bool {
    foreach ($positions as $p) {
      if ($p->rowIndex === $rook->rowIndex
          && $p->columnIndex === $rook->columnIndex) {
        return false;
      }
      if ($p->rowIndex === $rook->rowIndex) {
        return false;
      }
      if ($p->columnIndex === $rook->columnIndex) {
        return false;
      }
    }
    return true;
  }

  static function isSafeQueen(array $positions, $queen) : bool {
    if (!self::isSafeRook($positions, $queen)) {
      return false;
    }
    foreach ($positions as $p) {
      if ($p->leftDiagonal() === $queen->leftDiagonal()) {
        return false;
      }
      if ($p->rightDiagonal() === $queen->rightDiagonal()) {
        return false;
      }
    }
    return true;
  }
}

for ($N = 4; $N <= 14; $N++) {
  $s = microtime(true);
  $rr = Main::solveNQueensProblem($N);
  $e = microtime(true);
  $t = ($e - $s);
  $result = false;
  if (!empty($rr)) {
    $pop = array_pop($rr);
    $result = Test::isSafeQueen($rr, $pop);
  }
  $pad = $N < 10 ? ' ' : '';
  if ($result !== true) {
    echo "\033[31m";
    echo "ERROR N={$N} {$pad}in {$t}s";
    echo "\033[0m\n";
  } else {
    echo "\033[32m";
    echo "SUCCESS N={$N} {$pad}in {$t}s";
    echo "\033[0m\n";
  }
}

