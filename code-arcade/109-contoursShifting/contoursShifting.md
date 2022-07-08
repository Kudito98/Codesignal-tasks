<p>Mark got a rectangular array <code>matrix</code> for his birthday, and now he's thinking about all the fun things he can do with it. He likes shifting a lot, so he decides to shift all of its <em>i-contours</em> in a clockwise direction if <code>i</code> is even, and counterclockwise if <code>i</code> is odd.</p>
<p>Here is how Mark defines <em>i-contours</em>:</p>
<ul>
<li>the <em>0-contour</em> of a rectangular array as the union of left and right columns as well as top and bottom rows;</li>
<li>consider the initial matrix without the <em>0-contour</em>: its <em>0-contour</em> is the <em>1-contour</em> of the initial matrix;</li>
<li>define <em>2-contour</em>, <em>3-contour</em>, etc. in the same manner by removing <em>0-contours</em> from the obtained arrays.</li>
</ul>
<p>Implement a function that does exactly what Mark wants to do to his matrix.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For</p>
<pre><code>matrix = [[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16],
           [17, 18, 19, 20]]
</code></pre>
<p>the output should be</p>
<pre><code>solution(matrix) = [[ 5,  1,  2,  3],
                             [ 9,  7, 11,  4],
                             [13,  6, 15,  8],
                             [17, 10, 14, 12],
                             [18, 19, 20, 16]]
</code></pre>
</li>
<li>
<p>For <code>matrix = [[238, 239, 240, 241, 242, 243, 244, 245]]</code>,<br />
the output should be<br />
<code>solution(matrix) = [[245, 238, 239, 240, 241, 242, 243, 244]]</code>.</p>
<p>Note, that if a <em>contour</em> is represented by a <code>1 × n</code> array, its center is considered to be <em>below</em> it.</p>
</li>
<li>
<p>For</p>
<pre><code>matrix = [[238],
           [239],
           [240],
           [241],
           [242],
           [243],
           [244],
           [245]]
</code></pre>
<p>the output should be</p>
<pre><code>solution(matrix) = [[245],
                             [238],
                             [239],
                             [240],
                             [241],
                             [242],
                             [243],
                             [244]]
</code></pre>
<p>If a <em>contour</em> is represented by an <code>n × 1</code> array, its center is considered to be <em>to the left</em> of it.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.array.integer matrix</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ matrix.length ≤ 100</code>,<br />
<code>1 ≤ matrix[i].length ≤ 100</code>,<br />
<code>1 ≤ matrix[i][j] ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.array.integer</strong></p>
<p>The given <code>matrix</code> with its <em>contours</em> shifted.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
