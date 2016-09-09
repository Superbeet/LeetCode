public class Event implements Comparable<Event> {
	int time;
	int[] rect;

	public Event(int time, int[] rect) {
		this.time = time;
		this.rect = rect;
	}
	
	public int compareTo(Event that) {
		if (this.time != that.time) 
			return this.time - that.time;
		else 
			return this.rect[0] - that.rect[0];
	}
}

public boolean isRectangleCover(int[][] rectangles) {
	PriorityQueue<Event> pq = new PriorityQueue<Event> ();
        // border of y-intervals
	int[] border= {Integer.MAX_VALUE, Integer.MIN_VALUE};
	for (int[] rect : rectangles) {
		Event e1 = new Event(rect[0], rect);
		Event e2 = new Event(rect[2], rect);
		pq.add(e1);
		pq.add(e2);
		if (rect[1] < border[0]) border[0] = rect[1];
		if (rect[3] > border[1]) border[1] = rect[3];
	}
	TreeSet<int[]> set = new TreeSet<int[]> (new Comparator<int[]> () {
		@Override
                // if two y-intervals intersects, return 0
		public int compare (int[] rect1, int[] rect2) {
			if (rect1[3] <= rect2[1]) 
				return -1;
			else if (rect2[3] <= rect1[1]) 
				return 1;
			else 
				return 0;
		}
	});

	int yRange = 0;
	while (!pq.isEmpty()) {
		int time = pq.peek().time;
		while (!pq.isEmpty() && pq.peek().time == time) {
			Event e = pq.poll();
			int[] rect = e.rect;
			if (time == rect[2]) {
				set.remove(rect);
				yRange -= rect[3] - rect[1];
			} else {
				if (!set.add(rect)) 
					return false;
				yRange += rect[3] - rect[1];
			}
		}
        // check intervals
		if (!pq.isEmpty() && yRange != border[1] - border[0]) {
            return false;
			//if (set.isEmpty()) return false;
			//if (yRange != border[1] - border[0]) return false;
		}
	}
	return true;
}