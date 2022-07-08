<p>John has always had trouble remembering chess game positions. To help himself with remembering, he decided to store game positions in strings. He came up with the following position notation:</p>
<ul>
<li>The notation is built for the current game position row by row from top to bottom, with <code>'/'</code> separating each row notation;</li>
<li>Within each row, the contents of each square are described from the leftmost column to the rightmost;</li>
<li>Each piece is identified by a single letter taken from the standard English names (<code>'P'</code> = pawn, <code>'N'</code> = knight, <code>'B'</code> = bishop, <code>'R'</code> = rook, <code>'Q'</code> = queen, <code>'K'</code> = king);</li>
<li>White pieces are designated using upper-case letters (<code>"PNBRQK"</code>) while black pieces use lowercase (<code>"pnbrqk"</code>);</li>
<li>Empty squares are noted using digits <code>1</code> through <code>8</code> (the number of empty squares from the last piece);</li>
<li>Empty lines are noted as <code>"8"</code>.</li>
</ul>
<p>For example, for the initial position (shown in the picture below) the notation will look like this:</p>
<p><code>"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"</code></p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/chessNotation/img/initial.jpg?_tm=1624651524906" alt /></p>
<p>After the white pawn moves from <code>e2</code> to <code>e4</code>, the notation will be as follows:</p>
<p><code>"rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"</code></p>
<p>John has written down some positions using his <code>notation</code>, and now he wants to rotate the board <code>90</code> degrees clockwise and see what notation for the new board would look like. Help him with this task.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>notation = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"</code>, the output should be<br />
<code>solution(notation) = "RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr"</code>.</p>
<p>The notation corresponds to the initial position with one move made (white pawn from <code>e2</code> to <code>e4</code>).<br />
After rotating the board, it will look like this:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/chessNotation/img/example.jpg?_tm=1624651525201" alt /></p>
<p>So, the notation of the new position is <code>"RP4pr/NP4pn/BP4pb/QP4pq/K2P2pk/BP4pb/NP4pn/RP4pr"</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string notation</strong></p>
<p>Game position in John's notation. It is guaranteed that <code>notation</code> is correct, but not guaranteed that it represents a valid game position.</p>
<p><em>Guaranteed constraints:</em><br />
<code>15 ≤ notation.length ≤ 71</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>Notation for the position of the game board, rotated <code>90</code> degrees clockwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
