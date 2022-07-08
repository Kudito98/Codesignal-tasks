<p>Not long ago you got lost in the nearby woods when walking with your friend. You managed to get out of it, but no thanks to you: your friend was the one who drew the map of the woods and managed to find a way home. That embarrassed you quite a lot, so you decided to go out there to the other woods, get lost there and make your way home without any help.</p>
<p>The first part of your plan went smoothly, and now you're completely lost in unknown woods. You're on your own but for the map <code>wmap</code> you drew, and now you simply need to make it home, preferably before it gets too dark. To make things more interesting, you decided to find something unusual about the map you drew. Since you like even numbers even more than getting lost in the woods, you want to check if the map contains cycles only of even length. You firmly believe that such woods are magical, so you'll have something to tell your friend when you make it out safely.</p>
<p>Given the number of meadows in the woods <code>n</code> and the map representing their connections <code>wmap</code>, check if this map contains only cycles of even length.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>n = 5</code> and <code>wmap = [[1, 2], [1, 3], [1, 4], [0, 2], [4, 0]]</code>, the output should be<br />
<code>solution(n, wmap) = true</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isWoodMagical/img/example1.png?_tm=1624350039854" alt /></p>
<p>There is only one cycle: <code>1 - 4 - 0 - 2</code> and its length is <code>4</code>, which is an even number.</p>
</li>
<li>
<p>For <code>n = 5</code> and <code>wmap = [[1, 2], [1, 3], [1, 4], [0, 2], [4, 0], [1, 0]]</code>, the output should be<br />
<code>solution(n, wmap) = false</code>.</p>
<p><img src="https://codesignal.s3.amazonaws.com/tasks/isWoodMagical/img/example2.png?_tm=1624350040106" alt /></p>
<p>There is a cycle <code>1 - 4 - 0</code>, which length is <code>3</code> - an odd number.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer n</strong></p>
<p>The number of vertices on the map.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ n ≤ 10<sup>5</sup></code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer wmap</strong></p>
<p>Edges drawn on the map. <code>wmap[i]</code> for each valid <code>i</code> contains two elements and represents a road that connects <code>wmap[i][0]</code> and <code>wmap[i][1]</code>.<br />
It is guaranteed that between any two vertices there is no more than one edge.</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ wmap.length ≤ 96917</code>,<br />
<code>wmap[i].length = 2</code>,<br />
<code>0 ≤ wmap[i][j] &lt; n</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if there are only cycles with even length in the map and <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
