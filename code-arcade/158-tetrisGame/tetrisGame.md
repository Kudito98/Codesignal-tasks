<p>Let's play Tetris! But first we need to define the rules, especially since they probably differ from the way you've played Tetris before.</p>
<p>There is an empty field with <code>20</code> rows and <code>10</code> columns, which is initially empty. Random pieces appear on the field, each composed of four square blocks. You can't change the piece's shape, but you can rotate it <code>90</code> degree clockwise (possibly several times) and choose which columns it will appear within. Once you've rotated the piece and have set its starting position, it appears at the topmost row where you placed it and falls down until it can't fall any further. The objective of the game is to create horizontal lines composed of <code>10</code> blocks. When such a line is created, it disappears, and all lines above the deleted one move down. The player receives <code>1</code> point for each deleted row.</p>
<p>Your task is to implement an algorithm that places each new piece <em>optimally</em>. The piece is considered to be placed <em>optimally</em> if:</p>
<ul>
<li>The total number of blocks in the rows this piece will occupy after falling down is maximized;</li>
<li>Among all positions with that value maximized, this position requires the least number of rotations;</li>
<li>Among all positions that require the minimum number of rotations, this one is the leftmost one (i.e. the leftmost block's position is as far to the left as possible).</li>
</ul>
<p>The piece can't leave the field. It is guaranteed that it is always possible to place the Tetris piece in the field.</p>
<p>Implement this algorithm and calculate the number of points that you will get for the given set of <code>pieces</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>pieces = [[[".", "#", "."], 
           ["#", "#", "#"]],
          [["#", ".", "."], 
           ["#", "#", "#"]],
          [["#", "#", "."], 
           [".", "#", "#"]],
          [["#", "#", "#", "#"]],
          [["#", "#", "#", "#"]],
          [["#", "#"], 
           ["#", "#"]]]
</code></pre>
<p>the output should be<br />
<code>solution(pieces) = 1</code>.</p>
<p>For this explanation, we are representing each block by the index of the piece it belongs to. After the first 5 blocks fall, the field looks like this:</p>
<pre><code>...
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . 3 4
. . . . . . . . 3 4
. 0 . 1 . 2 2 . 3 4
0 0 0 1 1 1 2 2 3 4

</code></pre>
<p>Note that the <code>0<sup>th</sup></code>, <code>1<sup>st</sup></code>, and <code>2<sup>nd</sup></code> pieces all fell down without rotating, while the <code>3<sup>rd</sup></code> and the <code>4<sup>th</sup></code> pieces were rotated one time each.</p>
<p>Since there is now a row composed of <code>10</code> blocks, it is deleted, and you get <code>1</code> point.</p>
<p>When the last piece falls, the final field looks like this:</p>
<pre><code>...
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . . . . . . . . .
5 5 . . . . . . 3 4
5 5 . . . . . . 3 4
. 0 . 1 . 2 2 . 3 4

</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.array.char pieces</strong></p>
<p>A non-empty array of pieces in the order in which they fall. Each piece is represented as a rectangular matrix, where <code>'#'</code> represents a block and <code>'.'</code> represents an empty cell.</p>
<p>Each piece consists of <code>4</code> blocks, and each block shares a common side with at least one another block. It's guaranteed that each piece contains neither empty rows nor empty columns.</p>
<p><em>Guaranteed constraints:</em><br />
<code>3 ≤ pieces.length ≤ 30</code>,<br />
<code>1 ≤ pieces[i].length ≤ 2</code>,<br />
<code>2 ≤ pieces[i][j].length ≤ 4</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of points you will have by the end of the game.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
