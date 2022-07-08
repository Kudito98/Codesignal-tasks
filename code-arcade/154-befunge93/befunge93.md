<p>While exploring the ruins of a golden lost city, you discovered an ancient manuscript containing series of strange symbols. Thanks to your profound knowledge of dead languages, you realized that the text was written in one of the dialects of Befunge-93. Looks like the prophecy was true: you are the one who can find the answer to the Ultimate Question of Life! Of course you brought your futuristic laptop with you, so now you just need a function that will run the encrypted message and make you the all-knowing human being.</p>
<p>Befunge-93 is a stack-based programming language, the programs for which are arranged in a two-dimensional <em>torus</em> grid. The program execution sequence starts at the top left corner and proceeds to the right until the first direction instruction is met (which can appear in the very first cell). The <em>torus</em> adjective means that the program never leaves the grid: when it encounters a border, it simply goes to the next command at the opposite side of the grid.</p>
<p>You need to write a function that will be able to execute the given Befunge-93 <code>program</code>. Unfortunately your laptop, futuristic that it is, can't handle more than <code>10<sup>5</sup></code> instructions and will probably catch on fire if you try to execute more, so the function should exit after <code>10<sup>5</sup></code> commands. The good news is, the prophesy said that the answer to the Ultimate Question of Life contains no more than <code>100</code> symbols, so the function should return the <code>program</code> output once it contains <code>100</code> symbols.</p>
<p>The dialect of Befunge-93 in the manuscript consists of the following commands:</p>
<ul>
<li>direction instructions:
<ul>
<li><code>&gt;</code>: start moving right</li>
<li><code>&lt;</code>: start moving left</li>
<li><code>v</code>: start moving down</li>
<li><code>^</code>: start moving up</li>
<li><code>#</code>: bridge; skip next cell</li>
</ul>
</li>
<li>conditional instructions:
<ul>
<li><code>_</code>: pop a <code>value</code>; move right if <code>value = 0</code>, left otherwise</li>
<li><code>|</code>: pop a <code>value</code>; move down if <code>value = 0</code>, up otherwise</li>
</ul>
</li>
<li>math operators:
<ul>
<li><code>+</code>: addition; pop <code>a</code>, pop <code>b</code>, then push <code>a + b</code></li>
<li><code>-</code>: subtraction; pop <code>a</code>, pop <code>b</code>, then push <code>b - a</code></li>
<li><code>*</code>: multiplication; pop <code>a</code>, pop <code>b</code>, then push <code>a * b</code></li>
<li><code>/</code>: integer division; pop <code>a</code>, pop <code>b</code>, then push <code>b / a</code></li>
<li><code>%</code>: modulo operation; pop <code>a</code>, pop <code>b</code>, then push <code>b % a</code></li>
</ul>
</li>
<li>logical operators:
<ul>
<li><code>!</code>: logical NOT; pop a <code>value</code>, if the <code>value = 0</code>, push <code>1</code>, otherwise push <code>0</code></li>
<li><code>`</code>: greater than; pop <code>a</code> and <code>b</code>, then push <code>1</code> if <code>b &gt; a</code>, otherwise <code>0</code></li>
</ul>
</li>
<li>stack instructions:
<ul>
<li><code>:</code>: duplicate value on top of the stack</li>
<li><code>\</code>: swap the top stack value with the second to the top</li>
<li><code>$</code>: pop value from the stack and discard it</li>
</ul>
</li>
<li>output instructions:
<ul>
<li><code>.</code>: pop value and output it as an integer followed by a space</li>
<li><code>,</code>: pop value and output it as ASCII character</li>
</ul>
</li>
<li>digits <code>0-9</code>: push the encountered number on the stack</li>
<li><code>"</code>: start string mode; push each character's ASCII value all the way up to the next <code>"</code></li>
<li><code> </code> (whitespace character): empty instruction; does nothing</li>
<li><code>@</code>: end program; the program output should be returned then</li>
</ul>
<p>If the stack is empty and it is necessary to pop a value, no exception is raised; instead, <code>0</code> is produced.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>program = [
    "               v",
    "v  ,,,,,"Hello"&lt;",
    "&gt;48*,          v",
    ""!dlroW",,,,,,v&gt;",
    "25*,@         &gt; "
]
</code></pre>
<p>the output should be <code>solution(program) = "Hello World!\n"</code>.</p>
<p><em>Note, that in the tests tab you will see a <code>\</code> as an escape symbol before each <code>"</code></em>.</p>
<p>Here is how the program is executed:</p>
<ul>
<li>the program starts executing at the top left corner, doing nothing according to the <code> </code> command until it meets the <code>v</code> command, which makes the instructions direct it downward;</li>
<li>the <code>&lt;</code> makes it go left;</li>
<li>the <code>"</code> starts the string mode; <code>"Hello"</code> is pushed backwards on the stack;</li>
<li>six <code>,</code> symbols produce the <code>"Hello"</code> word, emptying the stack;</li>
<li>since the <code>v</code> symbol is encountered, the third line starts executing;</li>
<li><code>4</code> and <code>8</code> are pushed on the stack; the <code>*</code> operator pops them, multiplies and puts the result (<code>4 * 8 = 32</code>) back on the stack;</li>
<li>the <code>,</code> operator produces the character with the ASCII value of <code>32</code>, which is a whitespace character;</li>
<li>all the empty (<code>' '</code>) instructions are then executed, until the <code>v</code> command is encountered; then, the fourth line starts to execute;</li>
<li>the <code>&gt;</code> command forces instructions to the right to execute; since there is a border to the right, the leftmost instruction in the fourth line is executed next;</li>
<li>another string <code>"</code> mode starts, which pushes <code>"World!"</code> backwards on the stack;</li>
<li>next, the <code>,</code> commands output the <code>"World!"</code> string;</li>
<li>the <code>v</code> command moves command execution to the next line;</li>
<li>the <code>&gt;</code> command moves command execution to the very beginning of the fifth line;</li>
<li><code>2 * 5 = 10</code> is pushed on the stack, and produced as a character <code>\n</code>;</li>
<li>finally, <code>@</code> finishes the program execution.</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.string program</strong></p>
<p>Array of strings of an equal length, representing a correct program written in the Befunge-93 dialect. It is guaranteed that the program will not fail because of division by zero.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ program.length ≤ 20</code>,<br />
<code>1 ≤ program[0].length ≤ 100</code>,<br />
<code>program[i].length = program[0].length</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The output of the <code>program</code> after</p>
<ul>
<li>the program hits the <code>@</code> command;</li>
<li>the program executes <code>10<sup>5</sup></code> commands;</li>
<li>the program output contains <code>100</code> symbols;<br />
or whichever comes first.</li>
</ul>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
