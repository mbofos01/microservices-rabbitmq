import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.Channel;
import java.util.concurrent.TimeoutException;

public class Send {
   private final static String QUEUE_NAME = "some_queue";

   public static void main(String[] argv) throws java.io.IOException, TimeoutException {
      ConnectionFactory factory = new ConnectionFactory();
      factory.setHost("rabbitmq");  // Use the service name from Docker Compose
      Connection connection = factory.newConnection();
      Channel channel = connection.createChannel();
      channel.queueDeclare(QUEUE_NAME, false, false, false, null);

      // String message = "/shared/geko.jpg"; //"Hello World from Java!";
      String message = "{\"image_path\": \"/shared/geko.jpg\", \"size\": \"200\"}";

      channel.basicPublish("", QUEUE_NAME, null, message.getBytes());
      System.out.println(" [x] Sent '" + message + "'");

      channel.close();
      connection.close();
   }
}
