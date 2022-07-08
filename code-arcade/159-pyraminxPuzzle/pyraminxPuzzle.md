<p>You've mastered the Rubik's Cube and got bored solving it, so now you are looking for a new challenge. One puzzle similar to the Rubik's Cube caught your attention. It's called a <em>Pyraminx puzzle</em>, and is a triangular pyramid-shaped puzzle. The parts are arranged in a pyramidal pattern on each side, while the layers can be rotated with respect to each vertex, and the individual tips can be rotated as well. There are <code>4</code> faces on the Pyraminx. The puzzle should be held so that one face faces you and one face faces down, as in the image below. The four corners are then labeled U (for up), R (for right), L (for left), and B (for back). The front face thus contains the U, R, and L corners.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pyraminxPuzzle/img/notation.gif?_tm=1582081838371" alt /></p>
<p>Let's write down all possible moves for vertex <code>U</code> in the following notation:</p>
<ul>
<li><code>U</code> - <code>120°</code> counterclockwise turn of topmost tip (assuming that we're looking at the <em>pyraminx</em> from the top, and vertex <code>U</code> is the topmost);</li>
<li><code>U'</code> - clockwise turn for the same tip;</li>
<li><code>u</code> - <code>120°</code> counterclockwise turn of two upper layer;</li>
<li><code>u'</code> - clockwise turn for the same layers.</li>
</ul>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pyraminxPuzzle/img/moves.png?_tm=1582081838667" alt /></p>
<p>For other vertices the moves can be described similarly:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pyraminxPuzzle/img/moves.gif?_tm=1582081838954" alt /></p>
<p>The first puzzle you bought wasn't assembled, so you get your professional <em>pyraminx</em> solver friend to assemble it. He does, and you wrote down all his moves notated as described above. Now the puzzle's faces have colors <code>faceColors[0]</code> (front face), <code>faceColors[1]</code> (bottom face), <code>faceColors[2]</code> (left face), <code>faceColors[3]</code> (right face). You want to know the initial state of the puzzle to repeat your friend's moves and see how he solved it.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>faceColors = ['R', 'G', 'Y', 'O']</code> and <code>moves = ["B", "b'", "u'", "R"]</code>, the output should be</p>
<pre><code>solution(faceColors, moves) = [['Y', 'Y', 'Y', 'Y', 'R', 'R', 'R', 'R', 'G'],
                                     ['G', 'R', 'O', 'O', 'O', 'G', 'G', 'G', 'G'],
                                     ['Y', 'O', 'Y', 'G', 'O', 'O', 'G', 'G', 'Y'],
                                     ['R', 'O', 'O', 'R', 'O', 'Y', 'Y', 'R', 'R']]
</code></pre>
<p>Let's repeat the friend's steps in reverse order:</p>
<p>Final state:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pyraminxPuzzle/img/end.gif?_tm=1582081839198" alt /></p>
<p>Before the last move:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pyraminxPuzzle/img/move1.gif?_tm=1582081839480" alt /></p>
<p>One more move before that:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pyraminxPuzzle/img/move2.gif?_tm=1582081839723" alt /></p>
<p>And one more:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pyraminxPuzzle/img/move3.gif?_tm=1582081840042" alt /></p>
<p>Finally, the initial state:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pyraminxPuzzle/img/move4.gif?_tm=1582081840302" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.char faceColors</strong></p>
<p>A distinct array of four distinct characters, representing the front, bottom, left and right faces, respectively.</p>
<p><em>Guaranteed constraints:</em><br />
<code>faceColors.length = 4</code>.</p>
</li>
<li>
<p><strong>[input] array.string moves</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ moves.length ≤ 100</code>,</p>
 <pre><code>moves[i] ∈ {"U", "U'", "u", "u'", "L", "L'", "l", "l'", 
             "R", "R'", "r", "r'", "B", "B'", "b", "b'"}.</code></pre>
</li>
<li>
<p><strong>[output] array.array.char</strong></p>
<p>Initial state of the puzzle. <code>result[0]</code> should contain <code>9</code> characters corresponding to the front face, <code>result[1]</code> - to the bottom face, <code>result[2]</code> - to the left face and <code>result[3]</code> - to the right face.</p>
<p>The colors for each face should be given in top-to-bottom and left-to-right order, starting from the marked vertex (i.e. <code>U</code>, <code>B</code>, <code>L</code> or <code>R</code>), assuming that this vertex is at the top of the puzzle.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
