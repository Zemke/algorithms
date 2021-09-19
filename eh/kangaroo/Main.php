<?php
declare(strict_types=1);

function isCompletable(array $numbers) {
  return !is_null(getMinimalNumberOfJumps($numbers));
}

/**
 * Given an array of numbers the kangaroo may jump up to n numbers forward in the array
 * where n is the current element value. What's the least amount of jumps to reach the
 * end of the array.
 */
function getMinimalNumberOfJumps(array $numbers, &$jj = [], &$vv = [], &$add = 0, $parent=true) {
  echo 'numbers '; print_r($numbers);
  $end = min($numbers[0], count($numbers) - 1);
  for ($n = 1; $n <= $end; $n++) {
    echo "n $n\n";
    $id = $add + $n;
    echo "id $id\n";
    if (in_array($id, $vv)) {
      continue;
    }
    $vv[] = $id;
    $jumps = 1;
    if (($n + 1) === count($numbers)) { // hit the end
      echo "Could be $jumps\n";
      $jj[] = $jumps;
      print_r($jj);
      continue;
    } else if ($numbers[$n] === 0) { // too short
      continue;
    }
    $sub = getMinimalNumberOfJumps(array_slice($numbers, $n), $jj, $vv, ++$add, false);
    if (!is_null($sub)) {
      $jumps += $sub;
      if ($parent) {
        echo "Could be $jumps\n";
        $jj[] = $jumps;
      } else {
        return $jumps;
      }
    }
  }
  if (empty($jj)) {
    echo "uff\n";
    return 99;
  }
  return min($jj);
}


//$res = getMinimalNumberOfJumps([3,3,1,0,2]); // 2
//$res = getMinimalNumberOfJumps([3,1,1,0,2]); // null
$res = getMinimalNumberOfJumps([3,1,1,1,2]); // 2
//$res = getMinimalNumberOfJumps([1,1,0,1,2]);
//$res = getMinimalNumberOfJumps([2, 2, 0, 3, 1, 2, 0, 1]);
//$res = getMinimalNumberOfJumps([3,2,0,1,2]);
echo "res $res\n";


