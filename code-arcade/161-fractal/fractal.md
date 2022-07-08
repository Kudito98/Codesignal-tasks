<p>Your task is to draw a special solution after <code>n</code> iterations. The solution consists of <em>unit connectors</em> <code>'|'</code> and <code>'_'</code>.</p>
<p>For <code>n = 1</code> the solution looks as follows:</p>
<pre><code>_
_|
</code></pre>
<p>Now assume that you have already made <code>N</code> iterations and drawn the <code>f(N)</code> solution. To draw the <code>f(N + 1)</code> solution do the following:<br />
Note that every solution has exactly two edge points which can be connected to the edge points of other solutions using the <em>unit connectors</em>.<br />
At first, take the <code>f(N)</code> solution and place it in the top left corner. As the next step, put <code>f(N)</code> rotated by <code>0°, 90°, 180° or 270°</code> in the remaining 3 quarters - top right, bottom left and bottom right - so that it is possible to connect all four of them by adding exactly <code>3</code> unit connectors between the adjacent solution edge points.<br />
Note that there is always exactly one possible combination of rotations which allows to connect all <code>4</code> <code>f(N)</code> solutions together.</p>
<p>See examples below for better understanding.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>For <code>n = 1</code>, the output should be</li>
</ul>
<pre><code>solution(n) = [[' ', '_', ' '],       
              [' ', '_', '|']]
</code></pre>
<pre><code>In other words, it should represent      _
the following picture:                   _| 
</code></pre>
<ul>
<li>For <code>n = 2</code>, the output should be</li>
</ul>
<pre><code>solution(n) = [[' ', '_', ' ', ' ', ' ', '_', ' '],      
              [' ', '_', '|', ' ', '|', '_', ' '],                                  
              ['|', ' ', ' ', '_', ' ', ' ', '|'],                                 
              ['|', '_', '|', ' ', '|', '_', '|']]
</code></pre>
<pre><code>Or, to put it differently:  _   _
                            _| |_
                           |  _  |
                           |_| |_| 
</code></pre>
<ul>
<li>For <code>n = 3</code>, the output should be</li>
</ul>
<pre><code>solution(n) = [[" ", "_", " ", " ", " ", "_", "_", "_", " ", " ", " ", "_", "_", "_", " "], 
              [" ", "_", "|", " ", "|", "_", " ", " ", "|", "_", "|", " ", " ", "_", "|"], 
              ["|", " ", " ", "_", " ", " ", "|", " ", " ", "_", " ", " ", "|", "_", " "], 
              ["|", "_", "|", " ", "|", "_", "|", " ", "|", " ", "|", "_", "_", "_", "|"], 
              [" ", "_", " ", " ", " ", "_", " ", " ", "|", " ", " ", "_", "_", "_", " "], 
              ["|", " ", "|", "_", "|", " ", "|", " ", "|", "_", "|", " ", " ", "_", "|"], 
              ["|", "_", " ", " ", " ", "_", "|", " ", " ", "_", " ", " ", "|", "_", " "], 
              [" ", "_", "|", " ", "|", "_", "_", "_", "|", " ", "|", "_", "_", "_", "|"]]
</code></pre>
<p>The solution looks as follows:</p>
<pre><code>                      _   ___   ___ 
                      _| |_  |_|  _|
                     |  _  |  _  |_ 
                     |_| |_| | |___|
                      _   _  |  ___ 
                     | |_| | |_|  _|
                     |_   _|  _  |_ 
                      _| |___| |___|
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 6</code>.</p>
</li>
<li>
<p><strong>[output] array.array.char</strong></p>
<p>Each character can be an underscore (<code>'_'</code>), a vertical bar (<code>'|'</code>) or a whitespace character (<code>' '</code>).</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
