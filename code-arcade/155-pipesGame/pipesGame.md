<p>Carlos always loved playing video games, especially the well-known computer game "Pipes". Today he finally decided to write his own version of the legendary game from scratch.</p>
<p>In this game the player has to place the pipes on a rectangular field to make water pour from each source to a respective sink. He has already come up with the entire program, but one question still bugs him: how can he best check that the arrangement of pipes is correct?</p>
<p>It's your job to help him figure out exactly that.</p>
<p>Carlos has <code>7</code> types of pipes in his game, with numbers corresponding to each type:</p>
<ul>
<li><code>1</code> - vertical pipe</li>
<li><code>2</code> - horizontal pipe</li>
<li><code>3-6</code> - corner pipes</li>
<li><code>7</code> - two pipes crossed in the same cell (note that these pipes are not connected)</li>
</ul>
<p>Here they are, pipes <code>1</code> to <code>7</code>, respectively:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pipesGame/img/pipe_types.png?_tm=1624437059001" alt /></p>
<p>Water pours from each source in <strong>each</strong> direction that has a pipe connected to it (thus it can even pour in all four directions). The puzzle is solved correctly only if all water poured from each source eventually reaches a corresponding sink.</p>
<p>Help Carlos check whether the arrangement of pipes is correct. If it is correct, return the number of cells with pipes that will be full of water at the end of the game. If not, return <code>-X</code>, where <code>X</code> is the number of cells with water before the first leakage point is reached, or if the first drop of water reaches an incorrect destination (whichever comes first). Assume that water moves from one cell to another at the same speed.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>state = ["a224C22300000",
         "0001643722B00",
         "0b27275100000",
         "00c7256500000",
         "0006A45000000"]
</code></pre>
<p>the output should be <code>solution(state) = 19</code>.</p>
<p>Here is how the game will end:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/pipesGame/img/example.png?_tm=1624437059352" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string state</strong></p>
<p>Array of strings of an equal length representing some state of the game. The pipes are represented by the numbers <code>'1'</code> to <code>'7'</code>, the sources are given as lowercase English letters, and the corresponding sinks are marked by uppercase letters. Empty cells are marked with <code>'0'</code>.</p>
<p>It is guaranteed that each letter from the English alphabet either is not present in <code>state</code>, or appears there twice (in uppercase and lowercase).</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ state.length ≤ 100</code>,<br />
<code>1 ≤ state[i].length ≤ 100</code>,<br />
<code>state[i][j] ∈ {0-7, a-z, A-Z}</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>If the pipe arrangement is correct, return the number of cells with pipes that will be filled with water at the end of the game. If not, return <code>-X</code>, where <code>X</code> is the number of cells with water before the first leakage point is reached, or if the first drop of water reaches an incorrect destination.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
