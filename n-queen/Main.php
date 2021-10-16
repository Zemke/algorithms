<?php

declare(strict_types=1);

require('./Position.php');

class Main {

  static function solveNQueensProblem(int $N) : array {
    if ($N < 4) {
      return [];
    }

    $all = [];
    for ($i = 0; $i < $N; $i++) {
      for ($k = 0; $k < $N; $k++) {
        $all[] = new Position($i, $k);
      }
    }

    $data = [
      'left_diag' => [],
      'right_diag' => [],
      'cols' => [],
      'rows' => []
    ];

    $isSafeQueen = function ($p) use(&$data) {
      return !isset($data['left_diag'][$p->leftDiagonal()])
        && !isset($data['right_diag'][$p->rightDiagonal()])
        && !isset($data['cols'][$p->columnIndex])
        && !isset($data['rows'][$p->rowIndex]);
    };

    $rr = [];
    $reach = [0 => -1];
    $count_all = count($all);
    while (true) {
      for ($i = $reach[count($rr)]+1; $i < $count_all; $i++) {
        $count_rr = count($rr);
        $p = $all[$i];
        if ($isSafeQueen($p)) {
          $reach[$count_rr] = $i;
          $rr[] = $p;

          $data['left_diag'][$p->leftDiagonal()]++;
          $data['right_diag'][$p->rightDiagonal()]++;
          $data['cols'][$p->columnIndex]++;
          $data['rows'][$p->rowIndex]++;
        }
      }
      if (count($rr) === $N) {
        break;
      } else { // backtrack
        $backtrack = array_pop($rr);

        $data['left_diag'][$backtrack->leftDiagonal()]--;
        $data['right_diag'][$backtrack->rightDiagonal()]--;
        $data['cols'][$backtrack->columnIndex]--;
        $data['rows'][$backtrack->rowIndex]--;

        if ($data['left_diag'][$backtrack->leftDiagonal()] === 0) {
          unset($data['left_diag'][$backtrack->leftDiagonal()]);
        }
        if ($data['right_diag'][$backtrack->rightDiagonal()] === 0) {
          unset($data['right_diag'][$backtrack->rightDiagonal()]);
        }
        if ($data['cols'][$backtrack->columnIndex] === 0) {
          unset($data['cols'][$backtrack->columnIndex]);
        }
        if ($data['rows'][$backtrack->rowIndex] === 0) {
          unset($data['rows'][$backtrack->rowIndex]);
        }
      }
    }
    return $rr;
  }
}

if (!count(debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS))) {
  $N = intval($argv[1]);
  if ($N < 4) {
    echo "N should be at least 4\n";
    exit(2);
  }
  if (is_null($N)) {
    echo "N is not given\n";
    exit(1);
  }
  echo "Whoa, $N-Queens Problem processing...\n";
  $start = microtime(true);
  $rr = Main::solveNQueensProblem($N);
  $t = microtime(true) - $start;
  echo "Kids' stuff took me just {$t}s\n";
  for ($i = 0; $i < $N; $i++) {
    for ($k = 0; $k < $N; $k++) {
      echo in_array(new Position($i, $k), $rr) | "0";
      echo ' ';
    }
    echo "\n";
  }
}

