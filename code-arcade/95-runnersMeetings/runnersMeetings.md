<p>Some people run along a straight line in the same direction. They start simultaneously at pairwise distinct positions and run with constant speed (which may differ from person to person).</p>
<p>If two or more people are at the same point at some moment we call that a meeting. The number of people gathered at the same point is called meeting cardinality.</p>
<p>For the given starting positions and speeds of runners find the maximum meeting cardinality assuming that people run infinitely long. If there will be no meetings, return <code>-1</code> instead.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>startPosition = [1, 4, 2]</code> and <code>speed = [27, 18, 24]</code>, the output should be<br />
<code>solution(startPosition, speed) = 3</code>.</p>
<p>In 20 seconds after the runners start running, they end up at the same point. Check out the gif below for better understanding:</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/runnersMeetings/img/example.gif?_tm=1624665847040" alt /></p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer startPosition</strong></p>
<p>A non-empty array of integers representing starting positions of runners (in meters).</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ startPosition.length ≤ 100</code>,<br />
<code>-10<sup>4</sup> ≤ startPosition[i] ≤ 10<sup>4</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.integer speed</strong></p>
<p>Array of positive integers of the same length as <code>startPosition</code> representing speeds of the runners (in meters per minute).</p>
<p><em>Guaranteed constraints:</em><br />
<code>speed.length = startPosition.length</code>,<br />
<code>1 ≤ speed[i] ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The maximum meeting cardinality or <code>-1</code> if there will be no meetings.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
